import math
# Função para calcular as forças atuantes sobre o bloco:
def calcular_forcas(massa, angulo, coeficiente_atrito=0):
  """calcula as forças atuando em um bloco sobre um plano inclinado.
  Args:
  massa: Massa do bloco em kg.
  angulo: ângulo de inclinação do plano em graus.
  coeficiente_atrito: Coeficiente de atrito cinético.

  Returns:
    Um dicionário contendo as forças: peso, normal, atrito e resultante.
  """
  gravidade = 9.81  # Aceleração da gravidade em m/s^2
  angulo_radianos = math.radians(angulo)

  peso = massa * gravidade
  normal = peso * math.cos(angulo_radianos)
  atrito = coeficiente_atrito * normal
  resultante = peso * math.sin(angulo_radianos) - atrito


  return {
    'peso': peso,
    'normal': normal,
    'atrito': atrito,
    'resultante': resultante
  }
# Função para calcular a aceleração do bloco:
def calcular_aceleracao(forca_resultante, massa):
  """Calcula a aceleração resultante de um bloco.
  Args:
    forca_resultante: Força resultante em Newton.
    massa: Massa do bloco em kg.

  Returns:
    A aceleração resultante em m/s^2.
  """
  aceleracao = forca_resultante / massa
  return aceleracao

  Forcas = calcular_forcas(massa, angulo, coeficiente_atrito)
  aceleracao = calcular_aceleracao(Forcas['resultante'], massa)

if __name__ == '__main__':
  while True:
    try:
      massa = float(input("Digite a massa do bloco em kg: ").replace(',', '.'))
      angulo = float(input("Digite o ângulo de inclinação do plano em graus: ").replace(',', '.'))
      coeficiente_atrito = float(input("Digite o coeficiente de atrito cinético: ").replace(',', '.'))

      if massa <= 0 or angulo < 0 or angulo > 90 or coeficiente_atrito < 0:
        raise ValueError("Os valores de massa, ângulo e coeficiente de atrito devem ser maiores que zero.")


      forcas = calcular_forcas(massa, angulo, coeficiente_atrito)
      aceleracao = calcular_aceleracao(forcas['resultante'], massa)

      print("\n Resultados: ")
      print(f"Peso do bloco: {forcas['peso']:.2f} N")
      print(f"Força normal: {forcas['normal']:.2f} N")
      print(f"Força de atrito: {forcas['atrito']:.2f} N")
      print(f"Força resultante: {forcas['resultante']:.2f} N")
      print(f"Aceleração do bloco: {aceleracao:.2f} m/s²")
      print("\n")
      break

    except ValueError as e:
      print(f"Erro: {e}")
      print("Por favor, insira valores válidos.")
      print("\n")
      continue
