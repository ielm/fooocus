from enum import IntEnum, Enum

disabled = "Disabled"
enabled = "Enabled"
subtle_variation = "Vary (Subtle)"
strong_variation = "Vary (Strong)"
upscale_15 = "Upscale (1.5x)"
upscale_2 = "Upscale (2x)"
upscale_fast = "Upscale (Fast 2x)"

uov_list = [
    disabled,
    subtle_variation,
    strong_variation,
    upscale_15,
    upscale_2,
    upscale_fast,
]

CIVITAI_NO_KARRAS = [
    "euler",
    "euler_ancestral",
    "heun",
    "dpm_fast",
    "dpm_adaptive",
    "ddim",
    "uni_pc",
]

# fooocus: a1111 (Civitai)
KSAMPLER = {
    "euler": "Euler",
    "euler_ancestral": "Euler a",
    "heun": "Heun",
    "heunpp2": "",
    "dpm_2": "DPM2",
    "dpm_2_ancestral": "DPM2 a",
    "lms": "LMS",
    "dpm_fast": "DPM fast",
    "dpm_adaptive": "DPM adaptive",
    "dpmpp_2s_ancestral": "DPM++ 2S a",
    "dpmpp_sde": "DPM++ SDE",
    "dpmpp_sde_gpu": "DPM++ SDE",
    "dpmpp_2m": "DPM++ 2M",
    "dpmpp_2m_sde": "DPM++ 2M SDE",
    "dpmpp_2m_sde_gpu": "DPM++ 2M SDE",
    "dpmpp_3m_sde": "",
    "dpmpp_3m_sde_gpu": "",
    "ddpm": "",
    "lcm": "LCM",
    "tcd": "TCD",
}

SAMPLER_EXTRA = {"ddim": "DDIM", "uni_pc": "UniPC", "uni_pc_bh2": ""}

SAMPLERS = KSAMPLER | SAMPLER_EXTRA

KSAMPLER_NAMES = list(KSAMPLER.keys())

SCHEDULER_NAMES = [
    "normal",
    "karras",
    "exponential",
    "sgm_uniform",
    "simple",
    "ddim_uniform",
    "lcm",
    "turbo",
    "align_your_steps",
    "tcd",
    "edm_playground_v2.5",
]
SAMPLER_NAMES = KSAMPLER_NAMES + list(SAMPLER_EXTRA.keys())

sampler_list = SAMPLER_NAMES
scheduler_list = SCHEDULER_NAMES

clip_skip_max = 12

default_vae = "Default (model)"

refiner_swap_method = "joint"

cn_ip = "ImagePrompt"
cn_ip_face = "FaceSwap"
cn_canny = "PyraCanny"
cn_cpds = "CPDS"

ip_list = [cn_ip, cn_canny, cn_cpds, cn_ip_face]
default_ip = cn_ip

default_parameters = {
    cn_ip: (0.5, 0.6),
    cn_ip_face: (0.9, 0.75),
    cn_canny: (0.5, 1.0),
    cn_cpds: (0.5, 1.0),
}  # stop, weight

output_formats = ["png", "jpeg", "webp"]

inpaint_engine_versions = ["None", "v1", "v2.5", "v2.6"]
inpaint_option_default = "Inpaint or Outpaint (default)"
inpaint_option_detail = "Improve Detail (face, hand, eyes, etc.)"
inpaint_option_modify = "Modify Content (add objects, change background, etc.)"
inpaint_options = [inpaint_option_default, inpaint_option_detail, inpaint_option_modify]

desc_type_photo = "Photograph"
desc_type_anime = "Art/Anime"

sdxl_aspect_ratios = [
    "704*1408",
    "704*1344",
    "768*1344",
    "768*1280",
    "832*1216",
    "832*1152",
    "896*1152",
    "896*1088",
    "960*1088",
    "960*1024",
    "1024*1024",
    "1024*960",
    "1088*960",
    "1088*896",
    "1152*896",
    "1152*832",
    "1216*832",
    "1280*768",
    "1344*768",
    "1344*704",
    "1408*704",
    "1472*704",
    "1536*640",
    "1600*640",
    "1664*576",
    "1728*576",
]


class MetadataScheme(Enum):
    FOOOCUS = "fooocus"
    A1111 = "a1111"


metadata_scheme = [
    (f"{MetadataScheme.FOOOCUS.value} (json)", MetadataScheme.FOOOCUS.value),
    (f"{MetadataScheme.A1111.value} (plain text)", MetadataScheme.A1111.value),
]

controlnet_image_count = 4
preparation_step_count = 13


class OutputFormat(Enum):
    PNG = "png"
    JPEG = "jpeg"
    WEBP = "webp"

    @classmethod
    def list(cls) -> list:
        return list(map(lambda c: c.value, cls))


class PerformanceLoRA(Enum):
    Q1000 = None
    Q500 = None
    Q400 = None
    Q300 = None
    Q200 = None
    QUALITY = None
    SPEED = None
    EXTREME_SPEED = "sdxl_lcm_lora.safetensors"
    LIGHTNING = "sdxl_lightning_4step_lora.safetensors"
    HYPER_SD = "sdxl_hyper_sd_4step_lora.safetensors"


class Steps(IntEnum):
    Q1000 = 1000
    Q500 = 500
    Q400 = 400
    Q300 = 300
    Q200 = 200
    QUALITY = 100
    SPEED = 30
    EXTREME_SPEED = 8
    LIGHTNING = 4
    HYPER_SD = 4


class StepsUOV(IntEnum):
    Q1000 = 96
    Q500 = 64
    Q400 = 64
    Q300 = 56
    Q200 = 48
    QUALITY = 36
    SPEED = 18
    EXTREME_SPEED = 8
    LIGHTNING = 4
    HYPER_SD = 4


class Performance(Enum):
    Q1000 = "1000X"
    Q500 = "500X"
    Q400 = "400X"
    Q300 = "300X"
    Q200 = "200X"
    QUALITY = "Quality"
    SPEED = "Speed"
    EXTREME_SPEED = "Extreme Speed"
    LIGHTNING = "Lightning"
    HYPER_SD = "Hyper-SD"

    @classmethod
    def list(cls) -> list:
        return list(map(lambda c: c.value, cls))

    @classmethod
    def by_steps(cls, steps: int | str):
        return cls[Steps(int(steps)).name]

    @classmethod
    def has_restricted_features(cls, x) -> bool:
        if isinstance(x, Performance):
            x = x.value
        return x in [cls.EXTREME_SPEED.value, cls.LIGHTNING.value, cls.HYPER_SD.value]

    def steps(self) -> int | None:
        return Steps[self.name].value if self.name in Steps.__members__ else None

    def steps_uov(self) -> int | None:
        return StepsUOV[self.name].value if self.name in StepsUOV.__members__ else None

    def lora_filename(self) -> str | None:
        return (
            PerformanceLoRA[self.name].value
            if self.name in PerformanceLoRA.__members__
            else None
        )
