import oci
from .utils import LLMConfig
import importlib

class OCIGenAIClient():
    
    def __init__(self) -> None:
        self.__configs = LLMConfig()
        compartment_ = self.__configs.user.compartment_id
       
        userconfig_ = oci.config.from_file(self.__configs.user.userconfig,self.__configs.user.profile)
        
        ep_ = self.__configs.ocigenaiservice.endpoint
        
        self.client = oci.generative_ai_inference.GenerativeAiInferenceClient (
            config=userconfig_, 
            service_endpoint=ep_, 
            retry_strategy=oci.retry.NoneRetryStrategy(), 
            timeout=(10,240))
    
    def generate_text(self, prompt):  
        generate_text_detail = oci.generative_ai_inference.models.GenerateTextDetails()
        
        llm_inference_request = getattr(
                (importlib.import_module("oci.generative_ai_inference.models")),
                self.__configs.model.interface
            )()
        
        llm_inference_request.prompt = prompt
        llm_inference_request.max_tokens = self.__configs.model.params.max_tokens
        llm_inference_request.temperature = self.__configs.model.params.temperature
        
        generate_text_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(
            model_id=self.__configs.model.id
            )

        generate_text_detail.inference_request = llm_inference_request
        generate_text_detail.compartment_id = self.__configs.user.compartment_id
        generate_text_response = self.client.generate_text(generate_text_detail)
        
        return generate_text_response.data

        
if __name__ == "__main__":
    ociclinet = OCIGenAIClient()
    res = ociclinet.generate_text(prompt="Testing. Please respond if successful.")
    restext = res.inference_response.generated_texts[0].text
    print(restext)

