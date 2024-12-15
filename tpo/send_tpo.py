from datetime import datetime


async def send_tpo(phone_number, collection):
    document = collection.find_one({"phone_number": phone_number})

    if not document or datetime.utcnow() > document["expiresAt"]:
        return {"ok": False, "message": "TPO not found for this phone number"}

    return {"ok": True, "message": "TPO is valid", "tpo": document["tpo"]}
