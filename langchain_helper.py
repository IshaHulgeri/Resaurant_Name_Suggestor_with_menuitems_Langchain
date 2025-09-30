from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import random

# Using a reliable model that's available via Inference API
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"
MODEL_TASK = "text-generation"

def generate_restaurant_name_and_items(cuisine):
    """
    Generate restaurant name and menu items using Hugging Face model
    """
    try:
        # 1. Setup the Language Model (LLM)
        llm = HuggingFaceEndpoint(
            repo_id=MODEL_ID,
            temperature=0.95,  # Further increased for maximum creativity
            max_new_tokens=500,
            task=MODEL_TASK
        )
        
        # 2. Create the Prompt Template with stricter instructions for uniqueness
        prompt_template = PromptTemplate(
            input_variables=['cuisine'],
            template="""[INST] You are a highly creative restaurant naming expert with a flair for originality. 

Generate a completely unique, imaginative, and catchy restaurant name for a {cuisine} restaurant that is entirely distinct, avoiding any generic terms like 'Haven', 'Delight', 'Palace', or direct use of the cuisine name. The name should evoke a unique theme or story. Follow this with exactly 5 popular, specific, and highly diverse menu items relevant to {cuisine} cuisine, ensuring no repetition of items from previous suggestions and maximum variety.

Output format (follow exactly):
RESTAURANT NAME: [unique imaginative name here]
MENU ITEMS: [item1], [item2], [item3], [item4], [item5]

Example for Italian cuisine:
RESTAURANT NAME: Vesuvio's Ember
MENU ITEMS: Osso Buco, Ravioli al Tartufo, Frittata di Pasta, Polenta con Funghi, Sfogliatella

Now generate for {cuisine} cuisine: [/INST]""",
        )

        # 3. Create the LangChain
        chain = LLMChain(llm=llm, prompt=prompt_template)

        # 4. Run the Chain
        raw_response = chain.run(cuisine=cuisine)
        
        # 5. Parse the Response
        result = parse_response(raw_response)
        
        return result
        
    except Exception as e:
        print(f"Error in generate_restaurant_name_and_items: {e}")
        # Dynamic fallback with varied and unique names and items
        fallback_names = {
            "Indian": ["Taj Twilight", "Spice Odyssey", "Monsoon Feast", "Saffron Mirage", "Curry Cosmos"],
            "Italian": ["Tuscan Twilight", "Roman Rhapsody", "Venetian Veil", "Florentine Flame", "Sicilian Serenade"],
            "Mexican": ["Aztec Echo", "Maya Moon", "Teotihuacan Tale", "Oaxaca Oasis", "Salsa Symphony"],
            "Chinese": ["Dragon Whisper", "Peking Panorama", "Silk Road Saga", "Lotus Legend", "Chopstick Chronicle"],
            "Japanese": ["Sakura Secret", "Ninja Nectar", "Samurai Scroll", "Zen Zephyr", "Shogun Shadow"],
            "Thai": ["Jungle Jasmine", "Bangkok Breeze", "Temple Treasure", "Coconut Cove", "Pad Thai Parable"]
        }
        fallback_items = {
            "Indian": ["Chicken Korma", "Pulao", "Fish Curry", "Aloo Paratha", "Raita", "Malai Kofta", "Keema Naan"],
            "Italian": ["Gnocchi alla Romana", "Carpaccio", "Panzanella", "Tortellini in Brodo", "Zabaglione", "Agnolotti", "Stracciatella"],
            "Mexican": ["Barbacoa", "Ceviche", "Chilaquiles", "Sope", "Atole", "Pambazo", "Esquites"],
            "Chinese": ["Shredded Pork with Garlic Sauce", "Steamed Buns", "Hunan Beef", "Sesame Noodles", "Lychee Jelly", "Scallion Pancakes", "Braised Tofu"],
            "Japanese": ["Okonomiyaki", "Takoyaki", "Katsu Curry", "Shabu Shabu", "Daifuku", "Chawanmushi", "Yakisoba"],
            "Thai": ["Massaman Curry", "Larb Gai", "Khao Soi", "Mango Salad", "Fish Cakes", "Grilled Pork Neck", "Banana Fritters"]
        }
        name = random.choice(fallback_names.get(cuisine, ["Mystic Meal", "Golden Grove", "Emerald Eatery", "Crimson Kitchen", "Azure Annex"]))
        items = ", ".join(random.sample(fallback_items.get(cuisine, ["Dish 1", "Dish 2", "Dish 3", "Dish 4", "Dish 5", "Dish 6", "Dish 7"]), 5))
        return {
            "restaurant_name": name,
            "menu_items": items
        }


def parse_response(raw_response):
    """
    Parse the model response to extract restaurant name and menu items
    """
    result = {
        "restaurant_name": "Unique Restaurant",
        "menu_items": "Item 1, Item 2, Item 3, Item 4, Item 5"
    }
    
    try:
        # Clean the response
        response = raw_response.strip()
        lines = [line.strip() for line in response.split('\n') if line.strip()]
        
        for line in lines:
            if "RESTAURANT NAME:" in line.upper():
                name = line.split(":", 1)[1].strip()
                result["restaurant_name"] = name.strip('"\'')
            elif "MENU ITEMS:" in line.upper():
                items_str = line.split(":", 1)[1].strip()
                result["menu_items"] = items_str.strip('"\'').replace("  ", " ")
        
        # Ensure we have exactly 5 items
        items = [item.strip() for item in result["menu_items"].split(",")]
        if len(items) != 5:
            result["menu_items"] = ", ".join(items[:5] + ["Placeholder"] * (5 - len(items)))
            
    except Exception as e:
        print(f"Error parsing response: {e}")
        print(f"Raw response was: {raw_response[:200]}")
    
    return result