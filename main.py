import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions and create screen object
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Follow the Number")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Define font
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)


def generate_sequence(length):
    """Generate a random sequence of numbers with the specified length."""
    return [random.randint(1, 9) for _ in range(length)]


def display_message(message, font, color, y_offset=0):
    """Display a message in the center of the screen."""
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + y_offset))
    screen.blit(text, text_rect)


def display_sequence(sequence):
    """Display the sequence to the player."""
    screen.fill(black)
    display_message("Perhatikan urutan angka berikut:", small_font, white, -100)
    pygame.display.flip()
    pygame.time.delay(2000)

    for number in sequence:
        screen.fill(black)
        display_message(str(number), font, blue)
        pygame.display.flip()
        pygame.time.delay(1000)
        screen.fill(black)
        pygame.display.flip()
        pygame.time.delay(500)


def get_player_input(length):
    """Get the sequence from the player."""
    input_sequence = []
    input_active = True

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.unicode.isdigit():
                    input_sequence.append(int(event.unicode))
                    screen.fill(black)
                    display_message("Masukkan urutan angka:", small_font, white, -100)
                    display_message(' '.join(map(str, input_sequence)), font, blue)
                    pygame.display.flip()

    if len(input_sequence) != length:
        return None
    return input_sequence


def play_game():
    sequence_length = 3
    score = 0

    while True:
        sequence = generate_sequence(sequence_length)
        display_sequence(sequence)

        player_sequence = get_player_input(sequence_length)

        if player_sequence == sequence:
            score += 1
            sequence_length += 1
            screen.fill(black)
            display_message("Benar!", font, white)
            display_message(f"Skor Anda: {score}", small_font, white, 100)
            pygame.display.flip()
            pygame.time.delay(2000)
        else:
            screen.fill(black)
            display_message("Salah!", font, white)
            display_message(f"Urutan yang benar adalah: {' '.join(map(str, sequence))}", small_font, white, 100)
            display_message(f"Skor akhir Anda: {score}", small_font, white, 150)
            pygame.display.flip()
            pygame.time.delay(5000)
            break


if __name__ == "__main__":
    play_game()
    pygame.quit()
    sys.exit()
