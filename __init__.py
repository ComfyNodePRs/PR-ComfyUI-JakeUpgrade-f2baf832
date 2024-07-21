import shutil
import folder_paths
import os
from .nodes.jake_upgrade import *

def setup_js():
    import nodes
    js_dest_path = os.path.join(os.path.dirname(folder_paths.__file__), "web", "extensions", "jake_upgrade")

    if not os.path.exists(js_dest_path):
        os.makedirs(js_dest_path)

    js_src_path = os.path.join(os.path.join(os.path.dirname(__file__)), "js", "jake_upgrade.js")
    shutil.copy(js_src_path, js_dest_path)

setup_js()

# nodes.EXTENSION_WEB_DIRS["ComfyUI-Impact-Pack"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'js')

NODE_CLASS_MAPPINGS = {
    ### Misc Nodes
    "CR SD1.5 Aspect Ratio JK": CR_AspectRatioSD15_JK,
    "CR SDXL Aspect Ratio JK": CR_SDXLAspectRatio_JK,
    ### Reroute Nodes
    "Reroute List JK": RerouteList_JK,
    "Reroute Ckpt JK": RerouteCkpt_JK,
    "Reroute Vae JK": RerouteVae_JK,
    "Reroute Sampler JK": RerouteSampler_JK,
    "Reroute Upscale JK": RerouteUpscale_JK,
    "Reroute Resize JK": RerouteResize_JK,
    ### ControlNet Nodes
    "CR Apply ControlNet JK": CR_ApplyControlNet_JK,
    "CR Multi-ControlNet Stack JK": CR_ControlNetStack_JK,
    "CR Apply Multi-ControlNet JK": CR_ApplyControlNetStack_JK,
    ### LoRA Nodes
    "CR Load LoRA JK": CR_LoraLoader_JK,
    "CR LoRA Stack JK": CR_LoRAStack_JK,
    ### Embedding Nodes
    "Embedding Picker JK": EmbeddingPicker_JK,
    "Embedding Picker Multi JK": EmbeddingPicker_Multi_JK,
    ### Loader Nodes
    "Ckpt Loader JK": CkptLoader_JK,
    "Vae Loader JK": VaeLoader_JK,
    "Sampler Loader JK": SamplerLoader_JK,
    "Upscale Model Loader JK": UpscaleModelLoader_JK,
    ### Pipe Nodes
    "NodesState JK": NodesState_JK,
    "Ksampler Parameters JK": KsamplerParameters_JK,
    "Project Setting JK": ProjectSetting_JK,
    "Base Model Parameters JK": BaseModelParameters_JK,
    "Base Model Parameters Extract JK": BaseModelParametersExtract_JK,
    "Base Image Parameters Extract JK": BaseImageParametersExtract_JK,
    "Base Model Pipe JK": BaseModelPipe_JK,
    "Base Model Pipe Extract JK": BaseModelPipeExtract_JK,
    "Refine Pipe JK": RefinePipe_JK,
    "Refine Pipe Extract JK": RefinePipeExtract_JK,
    "Noise Injection Parameters JK": NoiseInjectionParameters_JK,
    "Refine Model Parameters JK": RefineModelParameters_JK,
    "Refine 1 Parameters Extract JK": Refine1ParametersExtract_JK,
    "Refine 2 Parameters Extract JK": Refine2ParametersExtract_JK,
    "Upscale Model Parameters JK": UpscaleModelParameters_JK,
    "Image Upscale Parameters Extract JK": ImageUpscaleParametersExtract_JK,
    "Latent Upscale Parameters Extract JK": LatentUpscaleParametersExtract_JK,
    "Upscale Model Parameters Extract JK": UpscaleModelParametersExtract_JK,
    "Detailer Parameters JK": DetailerParameters_JK,
    "Pipe End JK": PipeEnd_JK,
    "Metadata Pipe JK": MetadataPipe_JK,
    "Metadata Pipe Extract JK": MetadataPipeExtract_JK,
    ### Image Nodes
    "Save Image with Metadata JK": ImageSaveWithMetadata_JK,
    "Save Image with Metadata Flow JK": ImageSaveWithMetadata_Flow_JK,
    "Load Image With Metadata JK": LoadImageWithMetadata_JK,
    "HintImageEnchance JK": HintImageEnchance_JK,
    ### Animation Nodes
    "Animation Prompt JK": AnimPrompt_JK,
    "Animation Value JK": AnimValue_JK,
    ### Logic Switches Nodes
    "CR Boolean JK": CR_Boolean_JK,
    "CR Int Input Switch JK": CR_IntInputSwitch_JK,
    "CR Float Input Switch JK": CR_FloatInputSwitch_JK,
    "CR Image Input Switch JK": CR_ImageInputSwitch_JK,
    "CR Mask Input Switch JK": CR_MaskInputSwitch_JK,
    "CR Latent Input Switch JK": CR_LatentInputSwitch_JK,
    "CR Conditioning Input Switch JK": CR_ConditioningInputSwitch_JK,
    "CR Clip Input Switch JK": CR_ClipInputSwitch_JK,
    "CR Model Input Switch JK": CR_ModelInputSwitch_JK,
    "CR ControlNet Input Switch JK": CR_ControlNetInputSwitch_JK,
    "CR Text Input Switch JK": CR_TextInputSwitch_JK,
    "CR VAE Input Switch JK": CR_VAEInputSwitch_JK,
    "CR Switch Model and CLIP JK": CR_ModelAndCLIPInputSwitch_JK,
    "CR Pipe Input Switch JK": CR_PipeInputSwitch_JK,
    "CR Impact Pipe Input Switch JK": CR_ImpactPipeInputSwitch_JK,
    "CR Mesh Input Switch JK": CR_MeshInputSwitch_JK,
    "CR Orbit Pose Input Switch JK": CR_OrbitPoseInputSwitch_JK,
    ### ComfyMath Fix Nodes
    "CM_BoolToInt JK": BoolToInt_JK,
    "CM_IntToBool JK": IntToBool_JK,
    "CM_BoolUnaryOperation JK": BoolUnaryOperation_JK,
    "CM_BoolBinaryOperation JK": BoolBinaryOperation_JK,
    "CM_FloatUnaryCondition JK": FloatUnaryCondition_JK,
    "CM_FloatBinaryCondition JK": FloatBinaryCondition_JK,
    "CM_IntUnaryCondition JK": IntUnaryCondition_JK,
    "CM_IntBinaryCondition JK": IntBinaryCondition_JK,
    "CM_NumberUnaryCondition JK": NumberUnaryCondition_JK,
    "CM_NumberBinaryCondition JK": NumberBinaryCondition_JK,
    "CM_Vec2UnaryCondition JK": Vec2UnaryCondition_JK,
    "CM_Vec2BinaryCondition JK": Vec2BinaryCondition_JK,
    "CM_Vec2ToFloatUnaryOperation JK": Vec2ToFloatUnaryOperation_JK,
    "CM_Vec2ToFloatBinaryOperation JK": Vec2ToFloatBinaryOperation_JK,
    "CM_Vec2FloatOperation_JK": Vec2FloatOperation_JK,
    "CM_Vec3UnaryCondition JK": Vec3UnaryCondition_JK,
    "CM_Vec3BinaryCondition JK": Vec3BinaryCondition_JK,
    "CM_Vec3ToFloatUnaryOperation JK": Vec3ToFloatUnaryOperation_JK,
    "CM_Vec3ToFloatBinaryOperation JK": Vec3ToFloatBinaryOperation_JK,
    "CM_Vec3FloatOperation_JK": Vec3FloatOperation_JK,
    "CM_Vec4UnaryCondition JK": Vec4UnaryCondition_JK,
    "CM_Vec4BinaryCondition JK": Vec4BinaryCondition_JK,
    "CM_Vec4ToFloatUnaryOperation JK": Vec4ToFloatUnaryOperation_JK,
    "CM_Vec4ToFloatBinaryOperation JK": Vec4ToFloatBinaryOperation_JK,
    "CM_Vec4FloatOperation_JK": Vec4FloatOperation_JK,
    ### ComfyMath Nodes
    "CM_FloatToInt JK": FloatToInt_JK,
    "CM_IntToFloat JK": IntToFloat_JK,
    "CM_IntToNumber JK": IntToNumber_JK,
    "CM_NumberToInt JK": NumberToInt_JK,
    "CM_FloatToNumber JK": FloatToNumber_JK,
    "CM_NumberToFloat JK": NumberToFloat_JK,
    "CM_ComposeVec2 JK": ComposeVec2_JK,
    "CM_ComposeVec3 JK": ComposeVec3_JK,
    "CM_ComposeVec4 JK": ComposeVec4_JK,
    "CM_BreakoutVec2 JK": BreakoutVec2_JK,
    "CM_BreakoutVec3 JK": BreakoutVec3_JK,
    "CM_BreakoutVec4 JK": BreakoutVec4_JK,
    "CM_FloatUnaryOperation JK": FloatUnaryOperation_JK,
    "CM_FloatBinaryOperation JK": FloatBinaryOperation_JK,
    "CM_IntUnaryOperation JK": IntUnaryOperation_JK,
    "CM_IntBinaryOperation JK": IntBinaryOperation_JK,
    "CM_NumberUnaryOperation JK": NumberUnaryOperation_JK,
    "CM_NumberBinaryOperation JK": NumberBinaryOperation_JK,
    "CM_Vec2UnaryOperation JK": Vec2UnaryOperation_JK,
    "CM_Vec2BinaryOperation JK": Vec2BinaryOperation_JK,
    "CM_Vec3UnaryOperation JK": Vec3UnaryOperation_JK,
    "CM_Vec3BinaryOperation JK": Vec3BinaryOperation_JK,
    "CM_Vec4UnaryOperation JK": Vec4UnaryOperation_JK,
    "CM_Vec4BinaryOperation JK": Vec4BinaryOperation_JK,
    ### Simple Evaluate Nodes
    "Evaluate Ints JK": EvaluateInts_JK,
    "Evaluate Floats JK": EvaluateFloats_JK,
    "Evaluate Strings JK": EvaluateStrs_JK,
    "Evaluate Examples JK": EvalExamples_JK,
    ### 3D Nodes
    "Orbit Poses JK": OrbitPoses_JK,
    "OrbitLists to OrbitPoses JK": OrbitLists_to_OrbitPoses_JK,
    "OrbitPoses to OrbitLists JK": OrbitPoses_to_OrbitLists_JK,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    ### Misc Nodes
    "CR SD1.5 Aspect Ratio JK": "SD1.5 Aspect Ratio JK🐉",
    "CR SDXL Aspect Ratio JK": "SDXL Aspect Ratio JK🐉",
    ### Reroute Nodes
    "Reroute List JK": "Reroute List JK🐉",
    "Reroute Ckpt JK": "Reroute Ckpt JK🐉",
    "Reroute Vae JK": "Reroute Vae JK🐉",
    "Reroute Sampler JK": "Reroute Sampler JK🐉",
    "Reroute Upscale JK": "Reroute Upscale JK🐉",
    "Reroute Resize JK": "Reroute Resize JK🐉",
    ### ControlNet Nodes
    "CR Apply ControlNet JK": "Apply ControlNet JK🐉",
    "CR Multi-ControlNet Stack JK": "Multi-ControlNet Stack JK🐉",
    "CR Apply Multi-ControlNet JK": "Apply Multi-ControlNet JK🐉",
    ### LoRA Nodes
    "CR Load LoRA JK": "Load LoRA JK🐉",
    "CR LoRA Stack JK": "LoRA Stack JK🐉",
    ### Embedding Nodes
    "Embedding Picker JK": "Embedding Picker JK🐉",
    "Embedding Picker Multi JK": "Embedding Picker Multi JK🐉",
    ### Loader Nodes
    "Ckpt Loader JK": "Ckpt Loader JK🐉",
    "Vae Loader JK": "Vae Loader JK🐉",
    "Sampler Loader JK": "Sampler Loader JK🐉",
    "Upscale Model Loader JK": "Upscale Model Loader JK🐉",
    ### Pipe Nodes
    "NodesState JK": "Nodes State JK🐉",
    "Ksampler Parameters JK": "Ksampler Parameters JK🐉",
    "Project Setting JK": "Project Setting JK🐉",
    "Base Model Parameters JK": "Base Model Parameters JK🐉",
    "Base Model Parameters Extract JK": "Base Model Parameters Extract JK🐉",
    "Base Image Parameters Extract JK": "Base Image Parameters Extract JK🐉",
    "Base Model Pipe JK": "Base Model Pipe JK🐉",
    "Base Model Pipe Extract JK": "Base Model Pipe Extract JK🐉",
    "Refine Pipe JK": "Refine Pipe JK🐉",
    "Refine Pipe Extract JK": "Refine Pipe Extract JK🐉",
    "Noise Injection Parameters JK": "Noise Injection Parameters JK🐉",
    "Refine Model Parameters JK": "Refine Model Parameters JK🐉",
    "Refine 1 Parameters Extract JK": "Refine 1 Parameters Extract JK🐉",
    "Refine 2 Parameters Extract JK": "Refine 2 Parameters Extract JK🐉",
    "Upscale Model Parameters JK":"Upscale Model Parameters JK🐉",
    "Image Upscale Parameters Extract JK": "Image Upscale Parameters Extract JK🐉",
    "Latent Upscale Parameters Extract JK": "Latent Upscale Parameters Extract JK🐉",
    "Upscale Model Parameters Extract JK": "Upscale Model Parameters Extract JK🐉",
    "Detailer Parameters JK": "Detailer Parameters JK🐉",
    "Pipe End JK": "Pipe End JK🐉",
    "Metadata Pipe JK": "Metadata Pipe JK🐉",
    "Metadata Pipe Extract JK": "Metadata Pipe Extract JK🐉",
    ### Image Nodes
    "Save Image with Metadata JK": "Save Image With Metadata JK🐉",
    "Save Image with Metadata Flow JK": "Save Image With Metadata Flow JK🐉",
    "Load Image With Metadata JK": "Load Image With Metadata JK🐉",
    "HintImageEnchance JK": "Enchance And Resize Hint Images JK🐉",
    ### Animation Nodes
    "Animation Prompt JK": "Animation Prompt JK🐉",
    "Animation Value JK": "Animation Value JK🐉",
    ### Logic switches Nodes
    "CR Boolean JK": "Boolean JK🐉",
    "CR Image Input Switch JK": "Image Input Switch JK🐉",
    "CR Mask Input Switch JK": "Mask Input Switch JK🐉",
    "CR Int Input Switch JK": "Int Input Switch JK🐉",
    "CR Float Input Switch JK": "Float Input Switch JK🐉",
    "CR Latent Input Switch JK": "Latent Input Switch JK🐉",
    "CR Conditioning Input Switch JK": "Conditioning Input Switch JK🐉",
    "CR Clip Input Switch JK": "Clip Input Switch JK🐉",
    "CR Model Input Switch JK": "Model Input Switch JK🐉",
    "CR ControlNet Input Switch JK": "ControlNet Input Switch JK🐉",
    "CR Text Input Switch JK": "Text Input Switch JK🐉",
    "CR VAE Input Switch JK": "VAE Input Switch JK🐉",
    "CR Switch Model and CLIP JK": "Switch Model and CLIP JK🐉",
    "CR Pipe Input Switch JK": "Pipe Input Switch JK🐉",
    "CR Impact Pipe Input Switch JK": "Impact Pipe Input Switch JK🐉",
    "CR Mesh Input Switch JK": "Mesh Input Switch JK🐉",
    "CR Orbit Pose Input Switch JK": "Orbit Pose Input Switch JK🐉",
    ### ComfyMath Fix Nodes
    "CM_BoolToInt JK": "BoolToInt JK🐉",
    "CM_IntToBool JK": "IntToBool JK🐉",
    "CM_BoolUnaryOperation JK": "BoolUnaryOp JK🐉",
    "CM_BoolBinaryOperation JK": "BoolBinaryOp JK🐉",
    "CM_FloatUnaryCondition JK": "FloatUnaryCon JK🐉",
    "CM_FloatBinaryCondition JK": "FloatBinaryCon JK🐉",
    "CM_IntUnaryCondition JK": "IntUnaryCon JK🐉",
    "CM_IntBinaryCondition JK": "IntBinaryCon JK🐉",
    "CM_NumberUnaryCondition JK": "NumberUnaryCon JK🐉",
    "CM_NumberBinaryCondition JK": "NumberBinaryCon JK🐉",
    "CM_Vec2UnaryCondition JK": "Vec2UnaryCon JK🐉",
    "CM_Vec2BinaryCondition JK": "Vec2BinaryCon JK🐉",
    "CM_Vec2ToFloatUnaryOperation JK": "Vec2ToFloatUnaryOp JK🐉",
    "CM_Vec2ToFloatBinaryOperation JK": "Vec2ToFloatBinaryOp JK🐉",
    "CM_Vec2FloatOperation_JK": "Vec2FloatOp JK🐉",
    "CM_Vec3UnaryCondition JK": "Vec3UnaryCon JK🐉",
    "CM_Vec3BinaryCondition JK": "Vec3BinaryCon JK🐉",
    "CM_Vec3ToFloatUnaryOperation JK": "Vec3ToFloatUnaryOp JK🐉",
    "CM_Vec3ToFloatBinaryOperation JK": "Vec3ToFloatBinaryOp JK🐉",
    "CM_Vec3FloatOperation_JK": "Vec3FloatOp JK🐉",
    "CM_Vec4UnaryCondition JK": "Vec4UnaryCon JK🐉",
    "CM_Vec4BinaryCondition JK": "Vec4BinaryCon JK🐉",
    "CM_Vec4ToFloatUnaryOperation JK": "Vec4ToFloatUnaryOp JK🐉",
    "CM_Vec4ToFloatBinaryOperation JK": "Vec4ToFloatBinaryOp JK🐉",
    "CM_Vec4FloatOperation_JK": "Vec4FloatOp JK🐉",
    ### ComfyMath Nodes
    "CM_FloatToInt JK": "FloatToInt JK🐉",
    "CM_IntToFloat JK": "IntToFloat JK🐉",
    "CM_IntToNumber JK": "IntToNumber JK🐉",
    "CM_NumberToInt JK": "NumberToInt JK🐉",
    "CM_FloatToNumber JK": "FloatToNumber JK🐉",
    "CM_NumberToFloat JK": "NumberToFloat JK🐉",
    "CM_ComposeVec2 JK": "ComposeVec2 JK🐉",
    "CM_ComposeVec3 JK": "ComposeVec3 JK🐉",
    "CM_ComposeVec4 JK": "ComposeVec4 JK🐉",
    "CM_BreakoutVec2 JK": "BreakoutVec2 JK🐉",
    "CM_BreakoutVec3 JK": "BreakoutVec3 JK🐉",
    "CM_BreakoutVec4 JK": "BreakoutVec4 JK🐉",
    "CM_FloatUnaryOperation JK": "FloatUnaryOp JK🐉",
    "CM_FloatBinaryOperation JK": "FloatBinaryOp JK🐉",
    "CM_IntUnaryOperation JK": "IntUnaryOp JK🐉",
    "CM_IntBinaryOperation JK": "IntBinaryOp JK🐉",
    "CM_NumberUnaryOperation JK": "NumberUnaryOp JK🐉",
    "CM_NumberBinaryOperation JK": "NumberBinaryOp JK🐉",
    "CM_Vec2UnaryOperation JK": "Vec2UnaryOp JK🐉",
    "CM_Vec2BinaryOperation JK": "Vec2BinaryOp JK🐉",
    "CM_Vec3UnaryOperation JK": "Vec3UnaryOp JK🐉",
    "CM_Vec3BinaryOperation JK": "Vec3BinaryOp JK🐉",
    "CM_Vec4UnaryOperation JK": "Vec4UnaryOp JK🐉",
    "CM_Vec4BinaryOperation JK": "Vec4BinaryOp JK🐉",
    ### Simple Evaluate Nodes
    "Evaluate Ints JK": "Evaluate Ints JK🐉",
    "Evaluate Floats JK": "Evaluate Floats JK🐉",
    "Evaluate Strings JK": "Evaluate String JK🐉",
    "Evaluate Examples JK": "Evaluate Examples JK🐉",
    ### 3D Nodes
    "Orbit Poses JK": "Orbit Poses JK🐉",
    "OrbitLists to OrbitPoses JK": "OrbitLists to OrbitPoses JK🐉",
    "OrbitPoses to OrbitLists JK": "OrbitPoses to OrbitLists JK🐉",
}

__all__ = ['NODE_CLASS_MAPPINGS']

print("\033[34mJake Upgrade Nodes: \033[92m123 Nodes Loaded\033[0m")
