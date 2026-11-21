import httpx
from speechall.client import SpeechallApi


def test_list_models_decodes_unknown_catalog_values() -> None:
    catalog = [
        {
            "id": "futurecorp.model-x",
            "display_name": "FutureCorp Model X",
            "provider": "futurecorp",
            "model_type": "podcast",
            "accuracy_tier": "ultra",
            "is_available": True,
            "supports_srt": False,
            "supports_vtt": False,
        }
    ]

    def mock_catalog(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path.endswith("/speech-to-text-models")
        return httpx.Response(200, json=catalog)

    with httpx.Client(transport=httpx.MockTransport(mock_catalog)) as http_client:
        client = SpeechallApi(token="test-key", httpx_client=http_client)
        (model,) = client.speech_to_text.list_speech_to_text_models()

    assert model.id == "futurecorp.model-x"
    assert model.provider == "futurecorp"
    assert model.model_type == "podcast"
    assert model.accuracy_tier == "ultra"
