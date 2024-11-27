from sentence_transformers import SentenceTransformer, util
import pandas as pd

faq_data = pd.read_csv('faq_dataset.csv')

class ChatBot:
    def __init__(self) -> None:
        self.model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
        self.faq_embeddings = self.model.encode(faq_data['Question'].tolist(), convert_to_tensor=True)

        print('Bot initialized')
    
    def get_response(self, user_query):
        query_embedding = self.model.encode(user_query, convert_to_tensor=True)
        cosine_scores = util.pytorch_cos_sim(query_embedding, self.faq_embeddings).squeeze()
        best_match = cosine_scores.argmax().item()
        
        if cosine_scores[best_match] > 0.5:
            return faq_data['Answer'][best_match]
        else:
            return "Извините, я не знаю ответа на этот вопрос."


       