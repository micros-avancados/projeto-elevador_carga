# Projeto - Elevador de carga
# O seguinte projeto tem como objetivo fazer a implementação e configuração de um elevador de carga, que leva os respectivos produtos para os seus determinados andares.
# Um botão switch habilita/desabilita o funcionamento da esteira, e três sensores infravermelhos conectados à um Raspberry Pi farão a detecção dos produtos que serão descarregados da esteira para o elevador.
# Sensores infravermelhos também indicarão a localização do elevador em um andar. Um botão de acionamento momentâneo indica a descarga do produto do elevador, e o envia ao térreo.
# Logs serão salvos em outro Raspberry Pi em um banco de dados SQLite, contendo a data e hora que um produto foi descarregado, além de seu andar.
# A conexão entre as placas será feita via rede wireless, descartando o uso de cabos.
# A comunicação/interface com as placas será via monitor + teclado e mouse.
# As linguagens utilizadas serão (em sistema Raspbian):
C para leitura de sensores;
Java para controle e gerenciamento das informações + API para envio dos dados para banco de dados.
