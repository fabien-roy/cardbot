from app.sessions.ui.error_handler import SessionErrorHandler


def register_error_handlers(bot):
    bot.add_cog(SessionErrorHandler(bot))
