# Projeto - Sensor de carga
O seguinte projeto tem como objetivo fazer a implementação e configuração de um sensor de produtos, onde há um elevador que leva os respectivos produtos para os seus determinados andares. Uma esteira encaminha os produtos para o elevador, e três sensores ultrassônicos conectados à um Raspberry Pi farão a detecção dos produtos que serão descarregados da esteira para o elevador.
Logs serão salvos no Raspberry Pi em um banco de dados MySQL, contendo a data e hora que um produto foi detectado, além de seu andar. Outro Raspberry Pi conectará-se ao banco de dados e terá a capacidade de gerar tabelas com ou sem parâmetros, contendo o ID do pacote, a data/hora de sua detecção e o andar de destino.
# Conexão e interface de usuário
A conexão entre as placas será feita via rede wireless, descartando o uso de cabos. A comunicação/interface com as placas será via conexão remota, havendo a opção de monitor + teclado/mouse. As linguagens utilizadas serão (em sistema Raspbian):
Python para leitura de sensores;
Java para controle e gerenciamento das informações + API para leitura dos dados do banco de dados.
# Configuração dos dispositivos
Documentos de texto descrevem as etapas necessárias para a configuração do banco de dados, da leitura de sensores e quais pinos são utilizados para tal, além das configurações de rede e inicialização dos programas no dispositivo "monitor". Também há documentos de texto com as etapas de configuração para conexão ao banco de dados no "monitor", além do aplicativo para acesso ao banco e configurações de inicialização do dispositivo "viewer". Os códigos em Python estão comentados para fácil compreensão da aplicação.
# Sidenotes
O elevador é controlado por outro dispositivo, bem como o funcionamento da esteira. Este projeto apenas habilita e desabilita a esteira, sendo que seu funcionamento (funcionamento da esteira) está concentrado em outro circuito à parte do conjunto de sistemas referido neste documento.
