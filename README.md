# Calculadora de Amplificador BJT com Divisor de Tensão

Script Python para cálculo e verificação de ponto de operação e ganho de um amplificador BJT com polarização por divisor de tensão (configuração emissor comum).

## Objetivo

O script foi desenvolvido como apoio ao projeto de um circuito amplificador com transistor BJT (NPN) antes da montagem em laboratório. Com ele, é possível calcular antecipadamente os valores de tensão, corrente, resistência e ganho esperados, validando o dimensionamento do circuito e evitando erros na bancada.

## Circuito

O circuito projetado é um **amplificador de emissor comum** com polarização por divisor de tensão (R_B1 e R_B2), com os seguintes componentes principais:

| Componente | Valor |
|------------|-------|
| V_CC | 12 V |
| R_C | 500 Ω (dois resistores de 1kΩ em paralelo) |
| R_E | 1 kΩ |
| R_B1 | 100 kΩ |
| R_B2 | 47 kΩ |
| Capacitores de acoplamento | 220 nF |
| Frequência do sinal | 1 kHz |
| Sinal de entrada (v_i) | 1 mV |
| β (beta) do transistor | 100 |

## O que o script calcula

**Parâmetros DC (ponto de operação):**
- Correntes I_E, I_C e I_B
- Tensões V_B, V_E, V_C e V_CE
- Tensão e resistência de Thévenin da base (V_TH, R_TH)
- Verificação pelo método de Thévenin (I_E_Thev)

**Parâmetros do modelo de pequenos sinais:**
- Transcondutância g_m
- Resistência r_π (resistência de entrada do modelo π)
- Divisor de tensão entre r_π, R_TH e R_sig

**Ganho de tensão:**
- Calculado como `Av = -g_m · (r_π ∥ R_TH) / (r_π ∥ R_TH + R_sig) · R_C`

**Potências dissipadas** nos terminais do transistor (base, coletor, emissor).

## Como usar

Certifique-se de ter o Python instalado (versão 3.x):

```bash
python simulacao.py
```

Os resultados são impressos no terminal, organizados por categoria (resistências, tensões, correntes, potências e ganho).

## Resultado esperado (valores de referência)

Após a execução, os valores obtidos foram utilizados para:

1. Confirmar que o transistor opera na **região ativa** (V_CE > 0 e I_C > 0)
2. Verificar a consistência entre o ponto de operação calculado diretamente e pelo equivalente de Thévenin
3. Estimar o ganho de tensão esperado antes da medição em laboratório
4. Comparar os valores teóricos com as medições reais na bancada

## Observações

- O valor de `iE = 3 mA` foi definido como ponto de operação alvo no projeto
- A resistência `rSig = 50 Ω` representa a resistência interna da fonte de sinal
- O sinal negativo no ganho indica **inversão de fase** característica do amplificador de emissor comum
