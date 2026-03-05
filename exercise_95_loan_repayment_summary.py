import sys


def monthly_repayment(principal, annual_rate, months):
    monthly_rate = annual_rate / 100 / 12
    if monthly_rate == 0:
        return principal / months
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)


def total_repayment(monthly, months):
    return monthly * months


def main():
    principal = 10000
    annual_rate = 5
    months = 60

    monthly = monthly_repayment(principal, annual_rate, months)
    total = total_repayment(monthly, months)
    interest_paid = total - principal

    print(f"\n--- Loan Repayment Summary ---")
    print(f"Loan Amount:       ${principal:,.2f}")
    print(f"Monthly Repayment: ${monthly:,.2f}")
    print(f"Total Repayment:   ${total:,.2f}")
    print(f"Total Interest:    ${interest_paid:,.2f}")

    return 0


if __name__ == '__main__':
    sys.exit(main())

