"""
Student: Cesar Lanuza Urbina
Program: Bank accounts with deposits, withdrawals, and a minimum savings balance.
"""


class BankAccount:
    # Initialize the account with a nonnegative starting balance.
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("The starting balance cannot be negative.")
        self.balance = balance

    # Add a positive amount to the account balance.
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("The deposit amount must be positive.")
        self.balance += amount

    # Withdraw a positive amount only when sufficient funds are available.
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El retiro deber ser un numero positivo.")
        if amount > self.balance:
            raise ValueError("Fondos Insuficientes para esta transaccion. Consulte el balance")
        self.balance -= amount


class SavingsAccount(BankAccount):
    # Initialize the inherited balance and the required minimum balance.
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        if min_balance < 0:
            raise ValueError("Saldo minimo no puede ser negativo.")
        if balance < min_balance:
            raise ValueError("Balance inicial no puede ser menor que el saldo minimo..")
        
        self.min_balance = min_balance

    # Reject withdrawals that would leave the balance below the minimum.
    def withdraw(self, amount):
        # Check available funds before enforcing the minimum balance.
        if amount > self.balance:
            raise ValueError("Fondos Insuficientes para esta transaccion. Consulte el balance")
        if self.balance - amount < self.min_balance:
            raise ValueError(" El retiro no puede dejar el saldo por debajo del saldo minimo.")
        # Reuse the parent method to validate the amount and update the balance.
        super().withdraw(amount)


# Read a finite numeric amount, accepting either a decimal point or comma.
def read_amount(prompt):
    from math import isfinite

    while True:
        try:
            amount = float(input(prompt).strip().replace(",", "."))
            if not isfinite(amount):
                raise ValueError
            return amount
        except ValueError:
            print("Ingrese un numero valido y finito.")


# Create a savings account and manage it through an interactive menu.
def main():
    # Ask for valid initial values before creating the account.
    while True:
        balance = read_amount("Ingrese el saldo inicial: ")
        min_balance = read_amount("Ingrese el saldo minimo: ")
        try:
            account = SavingsAccount(balance, min_balance)
            break
        except ValueError as error:
            print(f"No se pudo crear la cuenta: {error}")

    # Keep the same account active until the user chooses to exit.
    while True:
        print("\n1. Consulta de Cuenta")
        print("2. Deposito a cuenta")
        print("3. Hacer un retiro")
        print("0. Salir")
        option = input("Seleccione una opcion: ").strip()

        if option == "1":
            # Display the current balance and the withdrawal limit.
            print()
            print(f"Saldo actual: {account.balance:.2f}")
            print(f"Saldo minimo: {account.min_balance:.2f}")
        elif option in ("2", "3"):
            amount = read_amount("Ingrese el monto: ")
            try:
                # Use the account methods to validate and apply the transaction.
                if option == "2":
                    account.deposit(amount)
                    print("Deposito realizado.")
                else:
                    account.withdraw(amount)
                    print("Retiro realizado.")
                print(f"Saldo actual: {account.balance:.2f}")
            except ValueError as error:
                # Report rejected transactions without ending the menu.
                print(f"Operacion rechazada: {error}")
        elif option == "0":
            print()
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opcion invalida. Seleccione 1, 2, 3 o 0.")


# Start the menu only when this file is executed directly.
if __name__ == "__main__":
    main()
