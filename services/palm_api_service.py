from services.interfaces.i_chatbot_api_service import IChatbotApiService


import google.generativeai as palm


class PalmApiService(IChatbotApiService):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_output(self, instructions: str) -> str:
        try:
            palm.configure(api_key=self.api_key)

            defaults = {
                "model": "models/text-bison-001",
                "temperature": 0.65,
                "candidate_count": 1,
                "top_k": 40,
                "top_p": 0.95,
                "max_output_tokens": 1024,
                "stop_sequences": [],
                "safety_settings": [
                    {"category": "DEROGATORY", "threshold": 1},
                    {"category": "TOXICITY", "threshold": 1},
                    {"category": "VIOLENCE", "threshold": 2},
                    {"category": "SEXUAL", "threshold": 2},
                    {"category": "MEDICAL", "threshold": 2},
                    {"category": "DANGEROUS", "threshold": 2},
                ],
            }

            response = palm.generate_text(**defaults, prompt=instructions)
            return response.result
        except Exception as e:
            raise e
