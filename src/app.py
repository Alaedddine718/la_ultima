from services.poll_service import PollService
from services.user_service import UserService
from services.nft_service import NFTService
from services.chatbot_service import ChatbotService

from repositories.encuesta_repo import EncuestaRepository
from repositories.usuario_repo import UsuarioRepository
from repositories.nft_repo import NFTRepository

from controllers.cli_controller import CLIController
from controllers.ui_controller import UIController
from ui.gradio_app import GradioApp

from config import cargar_config


