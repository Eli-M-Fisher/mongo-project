from fastapi import FastAPI, HTTPException
from .dal import MongoDAL, MongoQueryBuilder
from .models import SearchCriteria
from .processor import process_data
import os

app = FastAPI(title="Mongo Data Service")

# Load MongoDB Atlas connection from environment variables
MONGO_URI = os.getenv("MONGO_URI", "the-atlas-uri")
MONGO_DB = os.getenv("MONGO_DB", "the-database")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "the-collection")

dal = MongoDAL(MONGO_URI, MONGO_DB)
collection = dal.get_collection(MONGO_COLLECTION)


@app.get("/")
def root():
    return {"message": "Service is running"}


@app.get("/health")
def health_check():
    try:
        collection.find_one()
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/query")
def query(criteria: SearchCriteria):
    builder = MongoQueryBuilder(collection)

    if criteria.filters:
        for f in criteria.filters:
            builder.add_filter(f.field, f.operator, f.value)

    if criteria.or_conditions:
        or_blocks = []
        for group in criteria.or_conditions:
            conds = {f.field: {f"${f.operator}": f.value} for f in group}
            or_blocks.append(conds)
        builder.add_or_condition(or_blocks)

    if criteria.sort:
        builder.set_sort(criteria.sort.field, criteria.sort.direction)

    if criteria.limit:
        builder.set_limit(criteria.limit)

    if criteria.skip:
        builder.set_skip(criteria.skip)

    if criteria.projection:
        builder.set_projection(criteria.projection)

    docs = builder.execute()
    return process_data(docs)