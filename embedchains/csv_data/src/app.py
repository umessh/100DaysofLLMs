import os
# Replace this with your HF token
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "hf_XXX"

from embedchain import App

config = {
  'llm': {
    'provider': 'huggingface',
    'config': {
      'model': 'mistralai/Mistral-7B-Instruct-v0.2',
      'top_p': 0.5
    }
  },
  'embedder': {
    'provider': 'huggingface',
    'config': {
      'model': 'sentence-transformers/all-mpnet-base-v2'
    }
  }
}
app = App.from_config(config=config)
app.add("https://www.forbes.com/profile/elon-musk")
app.add("https://en.wikipedia.org/wiki/Elon_Musk")
x = app.query("What is the net worth of Elon Musk today?")
print(x)
# Answer: The net worth of Elon Musk today is $258.7 billion.
