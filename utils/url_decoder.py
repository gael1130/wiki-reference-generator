from googlenewsdecoder import new_decoderv1

def decode_google_news_link(google_link: str, interval_time: int = 5) -> str:
    try:
        decoded_url_result = new_decoderv1(google_link, interval=interval_time)
        if decoded_url_result.get("status"):
            return decoded_url_result["decoded_url"]
        raise ValueError(decoded_url_result["message"])
    except Exception as e:
        raise ValueError(f"Error decoding URL: {str(e)}")