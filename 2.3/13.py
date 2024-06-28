import uuid
from fastapi import FastAPI

from models import Feedback


app = FastAPI()
db_feedback = []

# uuid.uuid4()


@app.post('/feedback')
async def feedback_post(new_feedback: Feedback):
    db_feedback.append(
        {"id": new_feedback.id, "name": new_feedback.name, "message": new_feedback.message})
    return {"message": f"Feedback received. Thank you, {new_feedback.name}! Unsere id - {new_feedback.id}"}


@app.get("/all_feedback")
async def feedback_get():
    return db_feedback


@app.delete("/feedback_delete/{id}")
async def feedback_delete(id: int):
    for feedback in db_feedback:
        if feedback['id'] == id:
            db_feedback.remove(feedback)
            return {"message": f"Feedback mit id - {id} wird delitet- "}
    return {"message": f"Feedback existiert nicht"}

    # @app.get("feedback/{name}")
    # async def feedback_get_name(name: str):
    #     return db_feedback.get(name, f'User {name} nicht gefunden')
