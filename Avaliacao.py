#Nathalia Stigert

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

class Hospital(Pessoa):
    def __init__(self, nome, cnpj, chefe):
        super().__init__(nome)
        self._cnpj = cnpj
        self._chefe = chefe

    def getCNPJ(self):
        return self._cnpj

    def setCNPJ(self, cnpj):
        self._cnpj = cnpj

    def getChefe(self):
        return self._chefe.getNome()

    def setChefe(self, chefe):
        self._chefe = chefe

    def getEspecialidadeChefe(self):
        return self._chefe.getEspecialidade()

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self._cpf = cpf

    def getCPF(self):
        return self._cpf

    def setCPF(self, cpf):
        self._cpf = cpf

class Paciente(PessoaFisica):
    def __init__(self, nome, cpf, doenca, atendente):
        super().__init__(nome, cpf)
        self._doenca = doenca
        self._atendente = atendente
        self._plano = ""

    def getDoenca(self):
        return self._doenca

    def setDoenca(self, doenca):
        self._doenca = doenca

    def getAtendente(self):
        return self._atendente.getNome()

    def setAtendente(self, atendente):
        self._atendente = atendente

    def getPlano(self):
        if self._plano == "":
            return "Sem plano"
        else:
            return self._plano.getPlano()

    def setPlano(self, plano):
        self._plano = plano

class Medico(PessoaFisica):
    def __init__(self, nome, cpf, especialidade):
        super().__init__(nome, cpf)
        self._especialidade = especialidade
        self._hospital = ""

    def getEspecialidade(self):
        return self._especialidade.getEspecialidade()

    def setEspecialidade(self, especialidade):
        self._especialidade = especialidade

    def getHospital(self):
        if self._hospital == "":
            return self._hospital
        else:
            return self._hospital.getNome()

    def setHospital(self, hospital):
        self._hospital = hospital

class Especialidade:
    def __init__(self, especialidade):
        self._especialidade = especialidade

    def getEspecialidade(self):
        return self._especialidade

    def setEspecialidade(self, especialidade):
        self._especialidade = especialidade

class Plano:
    def __init__(self, nome):
        self._nome = nome

    def getPlano(self):
        return self._nome

    def setPlano(self, nome):
        self._nome = nome

especialidade1 = Especialidade("Cirurgião")
especialidade2 = Especialidade("Ortopedista")
medico1 = Medico("Medico1", "333.333.333-33", especialidade1)
medico2 = Medico("Medico2", "444.444.444-44", especialidade2)
paciente1 = Paciente("Paciente1", "111.111.111-11", "virose", medico1)
paciente2 = Paciente("Paciente2", "222.222.222-22", "covid", medico2)
hospital1 = Hospital("Hospital1", "11.111.111/1111-11", medico2)
medico1.setHospital(hospital1)
medico2.setHospital(hospital1)

print("Qual a especialidade do médico chefe de um hospital?")
print(hospital1.getEspecialidadeChefe())

print("\nQual o nome do hospital que um médico trabalha?")
print(medico1.getNome(), "-", medico1.getHospital())
print(medico2.getNome(), "-", medico2.getHospital())

print("\nQual o nome do médico que atende um paciente?")
print(paciente1.getNome(), "-", paciente1.getAtendente())
print(paciente2.getNome(), "-", paciente2.getAtendente())

print("\nQual o CPF de um paciente?")
print(paciente1.getNome(), "-", paciente1.getCPF())
print(paciente2.getNome(), "-", paciente2.getCPF())

print("\nQual o CNPJ de um hospital?")
print(hospital1.getCNPJ())

plano1 = Plano("Unimed")
paciente1.setPlano(plano1)
print("\nUtilização de nova classe:")
print("Qual o plano do paciente?")
print(paciente1.getNome(), "-", paciente1.getPlano())
print(paciente2.getNome(), "-", paciente2.getPlano())
