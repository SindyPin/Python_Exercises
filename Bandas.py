qty = int(input("Informe quantas bandas você gosta: "))

bands = []
for idx in range(0, qty):
    while True:
        band = input("Banda " + str(idx+1) + ": ")

        found = False
        for tmp in range(0, len(bands)):
            if bands[tmp] == band:
                found = True
                print("A banda " + band + " já foi informada antes... Vamos tentar de novo")

        if not found:
            bands.append(band)
            break

bandsRate = []
for idx in range(0, qty):
    bandRate = [bands[idx], 0]

    while True:
        bandRate[1] = float(input("Que nota você dá para a banda " + bands[idx] + "? "))
        if bandRate[1] >= 0 and bandRate[1] <= 10:
            break;
        print("Nota inválida (somente de 0 a 10)... Vamos tentar de novo")

    bandsRate.append(bandRate)

ratesSum = 0
for idx in range(0, qty):
    ratesSum += bandsRate[idx][1]
print("A média das notas dadas às bandas é " + str(ratesSum/qty))