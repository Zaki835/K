from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class ChatScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(orientation='vertical', **kwargs)

        # منطقة الرسائل
        self.chat_log_layout = GridLayout(cols=1, size_hint_y=None, spacing=5)
        self.chat_log_layout.bind(minimum_height=self.chat_log_layout.setter('height'))

        self.scroll_view = ScrollView(size_hint=(1, 0.85))
        self.scroll_view.add_widget(self.chat_log_layout)
        self.add_widget(self.scroll_view)

        # إدخال الرسالة وزر الإرسال
        input_layout = BoxLayout(size_hint=(1, 0.15))
        self.message_input = TextInput(hint_text="اكتب رسالتك هنا...", multiline=False)
        send_button = Button(text="إرسال")
        send_button.bind(on_press=self.send_message)

        input_layout.add_widget(self.message_input)
        input_layout.add_widget(send_button)
        self.add_widget(input_layout)

    def send_message(self, instance):
        message = self.message_input.text.strip()
        if message:
            label = Label(text=f"أنت: {message}", size_hint_y=None, height=30, halign='right', valign='middle')
            label.bind(size=label.setter('text_size'))
            self.chat_log_layout.add_widget(label)
            self.message_input.text = ""
            self.scroll_view.scroll_y = 0  # للتمرير إلى الأسفل


class ChatApp(App):
    def build(self):
        return ChatScreen()


if __name__ == "__main__":
    ChatApp().run()
