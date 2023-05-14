from fastapi.testclient import TestClient


def test_post_v1_english_words_generate_meaning(client: TestClient) -> None:
    response = client.get(url="/v1/english-words/generate-meaning?word=lambda")
    assert response.status_code == 200
    assert response.json() == {"meaning": "ギリシア文字の第11字母"}


def test_post_v1_english_words_generate_image(client: TestClient) -> None:
    response = client.get(url="/v1/english-words/generate-image?word=lambda")

    assert response.status_code == 200
    assert response.json() == {"image_url": "https://example.com/image.png"}
