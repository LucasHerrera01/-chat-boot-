# chat bot Impacto Têxtil > TECELAGEM < empresa que trabalho


print('Olá! Eu sou o chatbot da Impacto Têxtil, especializado em TECELAGEM. Como posso ajudá-lo hoje?')

while True:
    print('\n 1 - Conhecer nossos produtos')
    print('2 - Solicitar orçamento')
    print('3 - Consultar disponibilidade de malhas')
    print('4 - Falar com um atendente')
    print('5 - Sair')

    opcao = input('Digite o número da opção desejada: ')
    if opcao == '1':

        print('\n Trabalhamos com:')
        print('1 - Meia Malha')
        print('2 - Malhas Trabalhadas')
        print('3 - Ribanas')
        print('4 - Cotton')
        print('5 - Moletom')

    elif opcao == '2':
        print('\n Para solicitar um orçamento, por favor, envie uma mensagem para o nosso WhatsApp: +55 44 997270575. Nossa equipe entrará em contato com você o mais rápido possível.')

    elif opcao == '3':
        print('\n Para consultar a disponibilidade de Malhas, por favor, envie uma mensagem para o nosso WhatsApp: (44) 99959-2384. Nossa equipe responderá o mais rápido possível.')

    elif opcao == '4':
        print("Para falar com um atendente, entre em contato pelo WhatsApp:")
        print("WhatsApp: (44) 99959-2384")     
      

    elif opcao == '5':
        print('\n Obrigado por utilizar o chatbot da Impacto Têxtil. Tenha um ótimo dia!')
        break

    else:

        
        print('\n Opção inválida. Por favor, digite um número de 1 a 5.')
