"""
1. Princípio da Responsabilidade Única (SRP)
O SRP destaca a importância de uma classe ter uma única razão para mudar.
Isso significa que uma classe deve ter apenas uma responsabilidade.

A classe ManipuladorArquivo possui a responsabilidade única de lidar com operações de leitura e escrita em arquivos.
"""
class ManipuladorArquivo:
    def ler_arquivo(self, caminho):
        pass
    def salvar_arquivo(self, caminho, dados):
        pass


