from openai.types.chat import ChatCompletionSystemMessageParam

class ComplianceCheckService:
    def __init__(self, compliance_check_repository):
        self.compliance_check_repository = compliance_check_repository

    def check_compliance(self, compliance_check):
        messages = []
        messages.append(
            ChatCompletionSystemMessageParam(
                content=""
            )
        )
        return self.compliance_check_repository.achat_completion(model="gpt-4o")