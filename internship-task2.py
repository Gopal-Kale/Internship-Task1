def calculateConsultationFee(consultation_fee):
    return consultation_fee
def calculateRoomCharges(days, rate_per_day):
    return days * rate_per_day
def calculateMedicineBill(medicine_fee):
    return medicine_fee
def totalHospitalBill(consultation, room, medicine):
    consultation_amount = calculateConsultationFee(consultation)
    room_amount = calculateRoomCharges(room[0], room[1])
    medicine_amount = calculateMedicineBill(medicine)

    return consultation_amount + room_amount + medicine_amount
def calculateFinalBill(consultation, days, rate_per_day, medicine):
    total = totalHospitalBill(
        consultation,
        (days, rate_per_day),
        medicine
    )

    discount = total * 10 / 100
    final_amount = total - discount
    return final_amount
consultation_fee = 500
days = 3
rate_per_day = 1000
medicine_fee = 1000

total = totalHospitalBill(
    consultation_fee,
    (days, rate_per_day),
    medicine_fee
)
discount = total * 10 / 100
final_amount = calculateFinalBill(
    consultation_fee,
    days,
    rate_per_day,
    medicine_fee
)
print(f"Consultation Fee = {consultation_fee:.2f}")
print(f"Room Charges = {days * rate_per_day:.2f}")
print(f"Medicine Bill = {medicine_fee:.2f}")
print(f"Total Hospital Bill = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final Payable Amount = {final_amount:.2f}")