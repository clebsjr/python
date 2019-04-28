dia = int(input("Digite os dias: "))
hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))
segundo = int(input("Digite os segundos: "))

seg = segundo * 1
min_seg = minuto * 60
hora_seg = hora * 3600
dia_seg = dia * 86400

soma = seg + min_seg + hora_seg + dia_seg

print(f"{dia}dia(s) {hora}h{minuto}min{segundo}seg é igual a {soma}seg")