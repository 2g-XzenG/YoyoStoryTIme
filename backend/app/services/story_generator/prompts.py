from app.utils.config_loader import load_elements

def format_prompt(characters, scene):
    """
    Format extracted data into a structured prompt for story generation.
    """
    elements = load_elements()
    character_descriptions = [elements["characters"][char]["description"] for char in characters]
    scene_description = elements["scenes"][scene]["description"]

    # Create structured prompt
    prompt = f"这些角色分别是：{'; '.join(character_descriptions)}。故事发生的场景是：{scene_description}。"
    return prompt
