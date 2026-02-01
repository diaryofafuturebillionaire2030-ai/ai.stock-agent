from transformers import pipeline

# Load Hugging Face model (FREE)
generator = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=200
)

def generate_x_thread(stock, price, base, bull, bear):
    prompt = f"""
    Stock: {stock}
    Current Price: {price}
    Base Value: {base}
    Bull Value: {bull}
    Bear Value: {bear}

    Write a short Twitter (X) thread explaining this valuation.
    """
    return generator(prompt)[0]["generated_text"]


def generate_youtube_script(stock, price, base, bull, bear):
    prompt = f"""
    Create a YouTube script explaining the valuation of {stock}.
    Current Price: {price}
    Base Value: {base}
    Bull Value: {bull}
    Bear Value: {bear}
    """
    return generator(prompt)[0]["generated_text"]


def generate_instagram_caption(stock, price, base, bull, bear):
    prompt = f"""
    Write an Instagram caption about {stock} valuation.
    Current Price: {price}
    Base Value: {base}
    Bull Value: {bull}
    Bear Value: {bear}
    """
    return generator(prompt)[0]["generated_text"]
