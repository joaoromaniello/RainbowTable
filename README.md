# RainbowTable
Este é um projeto que visa criar uma ferramenta de quebra de senhas usando técnicas de RainbowTable em Python. Nesta implementação, as senhas utilizadas são números de telefone e personagens de Star Wars.

Para começar a usar o RainbowTable, basta clonar este repositório e instalar as dependências necessárias com o comando pip install -r requirements.txt. Em seguida, você pode executar o script principal *introInterface.py*. O código roda sob uma interface feita em TKinter.

O RainbowTable funciona da seguinte maneira:

1. Gera uma tabela com senhas possíveis, aplicando uma função de hash e uma função de redução em cada senha.
2. Armazena a tabela em um arquivo para uso futuro.
3. Quando é dada uma senha para ser quebrada, o RainbowTable aplica a mesma função de hash e função de redução que foram usadas na geração da tabela. Se a senha for encontrada na tabela, ela é exibida. Caso contrário, o processo é repetido até que a senha seja encontrada ou até que todas as entradas da tabela sejam verificadas.
Esperamos que você aproveite ao máximo o RainbowTable! Se tiver alguma dúvida ou sugestão, não hesite em abrir uma issue ou enviar um pull request.


Se tiver alguma dúvida ou sugestão, não hesite em abrir uma issue ou enviar um pull request.
