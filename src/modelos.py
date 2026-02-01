from dataclasses import dataclass

@dataclass
class TrabalhoAcademico:
    """Representa um registro de produção acadêmica."""
    programa: str
    orientador: str
    grande_area: str
    area: str
    titulo: str

    def __str__(self):
        return f"[{self.programa}] {self.titulo} (Orientador: {self.orientador})"