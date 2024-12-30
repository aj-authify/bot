import mongodb
import user


async def find_tpo(website):
    phone_number = user.user_data["phone_number"]
    if not phone_number:
        return {"ok": False, "message": "Phone number not found. Please /verify first"}

    document = mongodb.mongodb_data["collection"].find_one(
        {"phone_number": phone_number, "website": website}
    )

    if not document:
        return {
            "ok": False,
            "message": "TPO not found for this phone number and website",
        }

    return {"ok": True, "message": "TPO found", "document": document}
