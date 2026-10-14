from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Titular inválido")
        self._titular = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("Saldo inválido")
        self._saldo = valor

    @abstractmethod
    def sacar(self, valor):
        pass

    def __str__(self):
        return f"{self.titular} - Saldo: R$ {self.saldo:.2f}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.titular!r}, {self.saldo!r})"


class ContaCorrente(Conta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def sacar(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Saque inválido")
        if valor + 2 > self.saldo:
            raise ValueError("Saque inválido")
        self.saldo -= valor + 2

    def __str__(self):
        return f"Conta Corrente - {super().__str__()}"

    def __repr__(self):
        return f"ContaCorrente({self.titular!r}, {self.saldo!r})"


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def sacar(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Saque inválido")
        if valor > self.saldo:
            raise ValueError("Saque inválido")
        self.saldo -= valor

    def __str__(self):
        return f"Conta Poupança - {super().__str__()}"

    def __repr__(self):
        return f"ContaPoupanca({self.titular!r}, {self.saldo!r})"


class ContaSalario(Conta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def sacar(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Saque inválido")
        if valor > self.saldo:
            raise ValueError("Saque inválido")
        self.saldo -= valor

    def __str__(self):
        return f"Conta Salário - {super().__str__()}"

    def __repr__(self):
        return f"ContaSalario({self.titular!r}, {self.saldo!r})"


contas = [
    ContaCorrente("Ana", 1000),
    ContaPoupanca("Bruno", 1500),
    ContaSalario("Carla", 2000),
    ContaCorrente("Daniel", 800),
    ContaPoupanca("Eduarda", 1200),
    ContaSalario("Felipe", 900),
    ContaCorrente("Gabriela", 1700),
    ContaPoupanca("Henrique", 1100),
    ContaSalario("Isabela", 1400),
    ContaCorrente("João", 600),
]

print("CONTAS CADASTRADAS")

for conta in contas:
    print(conta)

print("\nDEMONSTRAÇÃO DE POLIMORFISMO")

for conta in contas:
    try:
        conta.sacar(100)
        print(f"{conta.__class__.__name__}: {conta}")
    except ValueError as erro:
        print(f"Erro: {erro}")

print("\nTESTE DE ENTRADA INVÁLIDA")

try:
    conta_invalida = ContaCorrente("", -100)
except ValueError as erro:
    print(f"Erro: {erro}")