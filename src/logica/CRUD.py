from sqlalchemy.orm import Session
from datetime import date
from Monelo import Usuario, Contraseña, Etiqueta, Sesion, ContraseñaEtiqueta


class UsuarioService:
    def __init__(self, session: Session):
        self.session = session

    def create_usuario(self, nombre_usuario, email, password, rol, fecha_registro=date.today()):
        usuario = Usuario(
            nombre_usuario=nombre_usuario,
            email=email,
            password=password,
            rol=rol,
            fecha_registro=fecha_registro
        )
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def get_usuario(self, usuario_id):
        return self.session.query(Usuario).filter_by(id_usuario=usuario_id).first()

    def update_usuario(self, usuario_id, **kwargs):
        usuario = self.get_usuario(usuario_id)
        if usuario:
            for key, value in kwargs.items():
                setattr(usuario, key, value)
            self.session.commit()
        return usuario

    def delete_usuario(self, usuario_id):
        usuario = self.get_usuario(usuario_id)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
        return usuario

class ContraseñaService:
    def __init__(self, session: Session):
        self.session = session

    def create_contraseña(self, servicio, nombre_usuario_servicio, contraseña_encriptada, id_usuario, fecha_creacion=date.today(), ultima_modificacion=date.today(), nota=""):
        contraseña = Contraseña(
            servicio=servicio,
            nombre_usuario_servicio=nombre_usuario_servicio,
            contraseña_encriptada=contraseña_encriptada,
            id_usuario=id_usuario,
            fecha_creacion=fecha_creacion,
            ultima_modificacion=ultima_modificacion,
            nota=nota
        )
        self.session.add(contraseña)
        self.session.commit()
        return contraseña

    def get_contraseña(self, contraseña_id):
        return self.session.query(Contraseña).filter_by(id_contraseña=contraseña_id).first()

    def update_contraseña(self, contraseña_id, **kwargs):
        contraseña = self.get_contraseña(contraseña_id)
        if contraseña:
            for key, value in kwargs.items():
                setattr(contraseña, key, value)
            self.session.commit()
        return contraseña

    def delete_contraseña(self, contraseña_id):
        contraseña = self.get_contraseña(contraseña_id)
        if contraseña:
            self.session.delete(contraseña)
            self.session.commit()
        return contraseña

class EtiquetaService:
    def __init__(self, session: Session):
        self.session = session

    def create_etiqueta(self, nombre):
        etiqueta = Etiqueta(nombre=nombre)
        self.session.add(etiqueta)
        self.session.commit()
        return etiqueta

    def get_etiqueta(self, etiqueta_id):
        return self.session.query(Etiqueta).filter_by(id_etiqueta=etiqueta_id).first()

    def update_etiqueta(self, etiqueta_id, **kwargs):
        etiqueta = self.get_etiqueta(etiqueta_id)
        if etiqueta:
            for key, value in kwargs.items():
                setattr(etiqueta, key, value)
            self.session.commit()
        return etiqueta

    def delete_etiqueta(self, etiqueta_id):
        etiqueta = self.get_etiqueta(etiqueta_id)
        if etiqueta:
            self.session.delete(etiqueta)
            self.session.commit()
        return etiqueta

class SesionService:
    def __init__(self, session: Session):
        self.session = session

    def create_sesion(self, id_usuario, fecha_inicio=date.today(), fecha_fin=None, ip=""):
        sesion = Sesion(
            id_usuario=id_usuario,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            ip=ip
        )
        self.session.add(sesion)
        self.session.commit()
        return sesion

    def get_sesion(self, sesion_id):
        return self.session.query(Sesion).filter_by(id_sesion=sesion_id).first()

    def update_sesion(self, sesion_id, **kwargs):
        sesion = self.get_sesion(sesion_id)
        if sesion:
            for key, value in kwargs.items():
                setattr(sesion, key, value)
            self.session.commit()
        return sesion

    def delete_sesion(self, sesion_id):
        sesion = self.get_sesion(sesion_id)
        if sesion:
            self.session.delete(sesion)
            self.session.commit()
        return sesion

class ContraseñaEtiquetaService:
    def __init__(self, session: Session):
        self.session = session

    def create_contraseña_etiqueta(self, id_contraseña, id_etiqueta):
        contraseña_etiqueta = ContraseñaEtiqueta(
            id_contraseña=id_contraseña,
            id_etiqueta=id_etiqueta
        )
        self.session.add(contraseña_etiqueta)
        self.session.commit()
        return contraseña_etiqueta

    def get_contraseña_etiqueta(self, contraseña_etiqueta_id):
        return self.session.query(ContraseñaEtiqueta).filter_by(id_contraseña_etiqueta=contraseña_etiqueta_id).first()

    def update_contraseña_etiqueta(self, contraseña_etiqueta_id, **kwargs):
        contraseña_etiqueta = self.get_contraseña_etiqueta(contraseña_etiqueta_id)
        if contraseña_etiqueta:
            for key, value in kwargs.items():
                setattr(contraseña_etiqueta, key, value)
            self.session.commit()
        return contraseña_etiqueta

    def delete_contraseña_etiqueta(self, contraseña_etiqueta_id):
        contraseña_etiqueta = self.get_contraseña_etiqueta(contraseña_etiqueta_id)
        if contraseña_etiqueta:
            self.session.delete(contraseña_etiqueta)
            self.session.commit()
        return contraseña_etiqueta
