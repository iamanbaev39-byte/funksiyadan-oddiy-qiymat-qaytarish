def toliq_ism_yasa(ism, familiya):
    return f"{ism.title()} {familiya.title()}"


talaba1 = toliq_ism_yasa('jonibek' , 'eshpolatov')
talaba2 = toliq_ism_yasa('eshpolatov' , 'jonibek')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")