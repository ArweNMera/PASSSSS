from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    rol = Column(String, nullable=False)
    fecha_registro = Column(Date)

    # Relaciones
    contraseñas = relationship("Contraseña", back_populates="usuario")
    sesiones = relationship("Sesion", back_populates="usuario")


class Contraseña(Base):
    __tablename__ = 'contraseñas'

    id_contraseña = Column(Integer, primary_key=True)
    servicio = Column(String, nullable=False)
    nombre_usuario_servicio = Column(String, nullable=False)
    contraseña_encriptada = Column(String, nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    fecha_creacion = Column(Date)
    ultima_modificacion = Column(Date)
    nota = Column(String)

    # Relaciones
    usuario = relationship("Usuario", back_populates="contraseñas")
    etiquetas = relationship("ContraseñaEtiqueta", back_populates="contraseña")


class Etiqueta(Base):
    __tablename__ = 'etiquetas'

    id_etiqueta = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    # Relaciones
    contraseñas = relationship("ContraseñaEtiqueta", back_populates="etiqueta")


class Sesion(Base):
    __tablename__ = 'sesiones'

    id_sesion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    ip = Column(String)

    # Relaciones
    usuario = relationship("Usuario", back_populates="sesiones")


class ContraseñaEtiqueta(Base):
    __tablename__ = 'contraseña_etiquetas'

    id_contraseña_etiqueta = Column(Integer, primary_key=True)
    id_contraseña = Column(Integer, ForeignKey('contraseñas.id_contraseña'))
    id_etiqueta = Column(Integer, ForeignKey('etiquetas.id_etiqueta'))

    # Relaciones
    contraseña = relationship("Contraseña", back_populates="etiquetas")
    etiqueta = relationship("Etiqueta", back_populates="contraseñas")
