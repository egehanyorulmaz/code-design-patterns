class RenderingEngine:
    def render(self):
        pass


class DirectXRenderingEngine(RenderingEngine):
    def render(self):
        print("Rendering using DirectX.")


class OpenGLRenderingEngine(RenderingEngine):
    def render(self):
        print("Rendering using OpenGL.")


class VulkanRenderingEngine(RenderingEngine):
    def render(self):
        print("Rendering using Vulkan.")


class RenderingEngineFactory:
    @staticmethod
    def create_engine(engine_type):
        if engine_type == 'DirectX':
            return DirectXRenderingEngine()
        elif engine_type == 'OpenGL':
            return OpenGLRenderingEngine()
        elif engine_type == 'Vulkan':
            return VulkanRenderingEngine()
        else:
            raise ValueError("Invalid rendering engine type")


# Client code
engine_type = 'OpenGL'  # You can switch between 'DirectX', 'OpenGL', 'Vulkan'
engine = RenderingEngineFactory.create_engine(engine_type)
engine.render()
