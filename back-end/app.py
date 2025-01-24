from fastapi import FastAPI
from pydantic import BaseModel
from tree import faq_tree
from fastapi.middleware.cors import CORSMiddleware
from rapidfuzz import fuzz, process

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    text: str

def preprocess_query(query):
    return query.lower().strip()


def find_answer(tree, query):
    if isinstance(tree, dict):
        keys = tree.keys()
        best_match = process.extractOne(query, keys, scorer=fuzz.partial_ratio)
        
        if best_match and best_match[1] > 60:
            result = find_answer(tree[best_match[0]], query)
            if result:  
                return result
        
        return f"Désolé, je n'ai pas trouvé de réponse précise pour '{query}'."
    
    elif isinstance(tree, list):
        return ", ".join(tree)
    
    elif isinstance(tree, str):
        return tree
    
    return None  

def generate_suggestions(tree, query):
    if isinstance(tree, dict):
        keys = tree.keys()
        suggestions = process.extract(query, keys, scorer=fuzz.partial_ratio, limit=3)
        return [s[0] for s in suggestions if s[1] > 40]
    return []

def create_paragraph(answer):
    return (
        f"Merci pour votre question !\n\n"
        f"En fonction de votre demande, voici quelques informations utiles :\n\n"
        f"{answer}\n\n"
        f"Si vous avez d'autres questions, n'hésitez pas à les poser !"
    )

@app.post("/ask")
async def ask_question(question: Question):
    query = preprocess_query(question.text)
    answer = find_answer(faq_tree, query)
    suggestions = generate_suggestions(faq_tree, query)

    if answer:
        enhanced_answer = create_paragraph(answer)
        return {
            "question": question.text,
            "answer": enhanced_answer,
            "suggestions": suggestions,
        }

    return {
        "question": question.text,
        "answer": "Désolé, je n'ai pas trouvé de réponse précise.",
        "suggestions": suggestions,
    }

@app.get("/")
async def read_root():
    return {"message": "Welcome to AskCampus!"}
