import re
import comfy

class RemoveThinkNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "remove_think"
    CATEGORY = "custom/text_processing"

    def remove_think(self, input_text):
        # 使用正则表达式全局匹配并移除所有<think>标签及其内容
        cleaned_text = re.sub(r'<think>.*?</think>', '', input_text, flags=re.DOTALL)
        # 移除首尾空白字符并确保至少返回空字符串
        return (cleaned_text.strip(),)

NODE_CLASS_MAPPINGS = {
    "RemoveThinkNode": RemoveThinkNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RemoveThinkNode": "去除思考"
}