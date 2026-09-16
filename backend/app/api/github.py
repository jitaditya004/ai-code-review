import hashlib
import hmac

from fastapi import APIRouter, Header, HTTPException, Request

from app.config import get_settings


router = APIRouter(
    prefix="/webhooks",
    tags=["GitHub"],
)

settings = get_settings()


def verify_github_signature(
    payload: bytes,
    signature: str | None,
) -> bool:

    if not signature:
        return False

    expected_signature = (
        "sha256="
        + hmac.new(
            settings.github_webhook_secret.encode(),
            payload,
            hashlib.sha256,
        ).hexdigest()
    )

    return hmac.compare_digest(
        expected_signature,
        signature,
    )


@router.post("/github")
async def github_webhook(
    request: Request,
    x_hub_signature_256: str | None = Header(default=None),
    x_github_event: str | None = Header(default=None),
):

    payload = await request.body()

    if not verify_github_signature(
        payload,
        x_hub_signature_256,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid GitHub signature",
        )

    return {
        "received": True,
        "event": x_github_event,
    }