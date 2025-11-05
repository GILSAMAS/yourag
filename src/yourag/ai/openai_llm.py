from openai import OpenAI
import os
from . import prompts

def get_openai_client() -> OpenAI:
    """
    Get the OpenAI client.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_API_KEY is None:
        print("OPENAI_API_KEY is not set in environment variables.")
        return None
    return OpenAI(api_key=OPENAI_API_KEY)


def get_embeddings(
    openai_client: OpenAI, text: str, model: str = "text-embedding-ada-002"
) -> Optional[List[float]]:
    """
    Get embeddings for a given text using OpenAI API.

    :param openai_client: The OpenAI client.
    :param text: The input text.
    :param model: The embedding model to use.
    :return: The embeddings as a list of floats.
    """
    try:
        response = openai_client.embeddings.create(input=[text], model=model)
        return response.data[0].embedding
    except Exception as e:
        print(f"Error getting embeddings: {e}")
        return None


def identify_category(user_prompt: str, openai_client) -> str:
    """
    Identify the category of a comment using OpenAI's GPT model.

    :param user_prompt: The input prompt.
    :param openai_client: The OpenAI client.
    :return: The generated response.
    """
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompts.CLASSIFICATION_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        print(response)
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        raise RuntimeError(f"Error calling LLM: {e}")


def generate_answer(question: str, context: str, openai_client) -> str:
    """
    Generate an answer using OpenAI's GPT model based on the question and context.

    :param question: The input question.
    :param context: The relevant context.
    :param openai_client: The OpenAI client.
    :return: The generated answer.
    """
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": prompts.YOUTUBE_COMMENT_REPLY_PROMPT,
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        print(response)
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        print(f"Error generating answer: {e}")
        return "I'm sorry, I couldn't generate an answer at this time."