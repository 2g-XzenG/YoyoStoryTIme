from backend.utils.config_loader import load_elements

def format_prompt(characters, scenes):
    """
    根据角色和场景数据生成一个结构化的 prompt，用于连续剧式故事生成。
    """
    elements = load_elements()
    character_descriptions = [
        elements["characters"][char]["description"] for char in characters
    ]
    scene_descriptions = [
        elements["scenes"][scene]["description"] for scene in scenes
    ]
    
    # 组装 prompt，强调每一部分的开放性结尾，便于续写
    prompt = (
        "请根据以下角色和场景创作一个充满悬念、连贯且具有连续剧风格的中文故事：\n\n"
        f"【角色】 { '; '.join(character_descriptions) }\n"
        f"【场景】 { '; '.join(scene_descriptions) }\n\n"
        "要求：\n"
        "1. 故事情节要连贯、细腻，每个部分都以开放式的结尾结束，留有悬念，便于后续续写。\n"
        "2. 人物性格鲜明，情感丰富。\n"
        "3. 故事语言优美、生动，吸引读者。"
    )
    return prompt