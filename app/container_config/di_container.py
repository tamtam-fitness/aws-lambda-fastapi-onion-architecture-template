from injector import Injector

from core.singleton import Singleton

from .module import RepositoryModule


class DIContainer(Singleton):
    MODULES = [RepositoryModule]
    injector: Injector = Injector(MODULES)

    # container_config.get()に引数を渡すと依存関係を解決してインスタンスを生成する
    # 依存関係はmoduleにてbindしている
    def resolve(self, cls: object) -> object:
        return self.injector.get(cls)
