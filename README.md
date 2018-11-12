# Projeto - Elevador de carga
# O seguinte projeto tem como objetivo fazer a implementação e configuração de um sensor de produtos, onde há um elevador que leva os respectivos produtos para os seus determinados andares.
# Uma esteira encaminha os produtos para o elevador, e três sensores infravermelhos conectados à um Raspberry Pi farão a detecção dos produtos que serão descarregados da esteira para o elevador.
# Logs serão salvos no Raspberry Pi em um banco de dados MySQL, contendo a data e hora que um produto foi detectado, além de seu andar.
# Outro Raspberry Pi conectará-se ao banco de dados e terá a capacidade de gerar tabelas com ou sem parâmetros, contendo o ID do pacote, a data/hora de sua detecção e o andar de destino.
# A conexão entre as placas será feita via rede wireless, descartando o uso de cabos.
# A comunicação/interface com as placas será via monitor + teclado e mouse.
# As linguagens utilizadas serão (em sistema Raspbian):
Python para leitura de sensores;
Java para controle e gerenciamento das informações + API para envio dos dados para banco de dados.
