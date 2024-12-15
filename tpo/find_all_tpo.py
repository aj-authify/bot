from datetime import datetime
import mongodb


async def get_valid_data(phone_number):
    valid_documents = []
    documents = mongodb.mongodb_data["collection"].find({"phone_number": phone_number})

    for document in documents:
        if datetime.utcnow() <= document["expiresAt"]:
            valid_documents.append(document)

    return valid_documents


async def find_all_tpo(phone_number):
    valid_documents = await get_valid_data(phone_number)

    if not valid_documents:
        return {"ok": False, "message": "TPO not found for this phone number"}

    return {"ok": True, "message": "TPOs are valid", "documents": valid_documents}
