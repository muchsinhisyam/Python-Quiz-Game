import sys, pygame

def check_events(ai_settings, button, sb):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mouse_click(ai_settings, button, mouse_x, mouse_y, sb)

def check_mouse_click(ai_settings, button, mouse_x, mouse_y, sb):
    play_button_clicked = button.rect_play.collidepoint(mouse_x, mouse_y)
    play_again_clicked = button.rect_play_again.collidepoint(mouse_x, mouse_y)
    next_clicked = button.rect_next.collidepoint(mouse_x, mouse_y)
    operators_clicked = button.rect_operators.collidepoint(mouse_x, mouse_y)
    array_clicked = button.rect_array.collidepoint(mouse_x, mouse_y)
    loops_clicked = button.rect_loops.collidepoint(mouse_x, mouse_y)

    answer_a_clicked = button.rect_answer1_a.collidepoint(mouse_x, mouse_y)
    answer_b_clicked = button.rect_answer1_b.collidepoint(mouse_x, mouse_y)
    answer_c_clicked = button.rect_answer1_c.collidepoint(mouse_x, mouse_y)

    # For number 11-15
    answer_a_clicked1 = button.rect_answer11_a.collidepoint(mouse_x, mouse_y)
    answer_b_clicked1 = button.rect_answer11_b.collidepoint(mouse_x, mouse_y)
    answer_c_clicked1 = button.rect_answer11_c.collidepoint(mouse_x, mouse_y)

    if play_button_clicked and ai_settings.menu == "main":
        ai_settings.menu = "tutorial"
    elif ai_settings.menu == "tutorial":
        if next_clicked:
            ai_settings.menu = "topics"
    elif ai_settings.menu == "topics":
        if operators_clicked:
            ai_settings.menu = "operators_no1"
        if array_clicked:
            ai_settings.menu = "array_no1"
        if loops_clicked:
            ai_settings.menu = "loops_no1"
    elif ai_settings.menu == "array_no1":
        if answer_a_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "array_no2"
        if answer_b_clicked:
            sb.wrong += 1
            ai_settings.menu = "array_no2"
        if answer_c_clicked:
            sb.wrong += 1
            ai_settings.menu = "array_no2"
    elif ai_settings.menu == "array_no2":
        if answer_a_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "array_no3"
        if answer_b_clicked:
            sb.wrong += 1
            ai_settings.menu = "array_no3"
        if answer_c_clicked:
            sb.wrong += 1
            ai_settings.menu = "array_no3"
    elif ai_settings.menu == "array_no3":
        if answer_a_clicked:
            sb.wrong += 1
            ai_settings.menu = "array_no4"
        if answer_b_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "array_no4"
        if answer_c_clicked:
            sb.wrong += 1
            ai_settings.menu = "array_no4"
    elif ai_settings.menu == "array_no4":
        if answer_a_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "array_no5"
        if answer_b_clicked:
            sb.wrong += 1
            ai_settings.menu = "array_no5"
        if answer_c_clicked:
            sb.wrong += 1
            ai_settings.menu = "array_no5"
    elif ai_settings.menu == "array_no5":
        if answer_a_clicked:
            sb.wrong += 1
            ai_settings.menu = "score"
        if answer_b_clicked:
            sb.wrong += 1
            ai_settings.menu = "score"
        if answer_c_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "score"
    elif ai_settings.menu == "operators_no1":
        if answer_a_clicked:
            sb.wrong += 1
            ai_settings.menu = "operators_no2"
        if answer_b_clicked:
            sb.wrong += 1
            ai_settings.menu = "operators_no2"
        if answer_c_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "operators_no2"
    elif ai_settings.menu == "operators_no2":
        if answer_a_clicked:
            sb.wrong += 1
            ai_settings.menu = "operators_no3"
        if answer_b_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "operators_no3"
        if answer_c_clicked:
            sb.wrong += 1
            ai_settings.menu = "operators_no3"
    elif ai_settings.menu == "operators_no3":
        if answer_a_clicked:
            sb.wrong += 1
            ai_settings.menu = "operators_no4"
        if answer_b_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "operators_no4"
        if answer_c_clicked:
            sb.wrong += 1
            ai_settings.menu = "operators_no4"
    elif ai_settings.menu == "operators_no4":
        if answer_a_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "operators_no5"
        if answer_b_clicked:
            sb.wrong += 1
            ai_settings.menu = "operators_no5"
        if answer_c_clicked:
            sb.wrong += 1
            ai_settings.menu = "operators_no5"
    elif ai_settings.menu == "operators_no5":
        if answer_a_clicked:
            sb.wrong += 1
            ai_settings.menu = "score"
        if answer_b_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "score"
    elif ai_settings.menu == "loops_no1":
        if answer_a_clicked1:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "loops_no2"
        if answer_b_clicked1:
            sb.wrong += 1
            ai_settings.menu = "loops_no2"
        if answer_c_clicked1:
            sb.wrong += 1
            ai_settings.menu = "loops_no2"
    elif ai_settings.menu == "loops_no2":
        if answer_a_clicked1:
            sb.wrong += 1
            ai_settings.menu = "loops_no3"
        if answer_b_clicked1:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "loops_no3"
        if answer_c_clicked1:
            sb.wrong += 1
            ai_settings.menu = "loops_no3"
    elif ai_settings.menu == "loops_no3":
        if answer_a_clicked1:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "loops_no4"
        if answer_b_clicked1:
            sb.wrong += 1
            ai_settings.menu = "loops_no4"
        if answer_c_clicked1:
            sb.wrong += 1
            ai_settings.menu = "loops_no4"
    elif ai_settings.menu == "loops_no4":
        if answer_a_clicked1:
            sb.wrong += 1
            ai_settings.menu = "loops_no5"
        if answer_b_clicked1:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "loops_no5"
        if answer_c_clicked1:
            sb.wrong += 1
            ai_settings.menu = "loops_no5"
    elif ai_settings.menu == "loops_no5":
        if answer_a_clicked:
            sb.wrong += 1
            ai_settings.menu = "score"
        if answer_b_clicked:
            sb.wrong += 1
            ai_settings.menu = "score"
        if answer_c_clicked:
            sb.correct += 1
            sb.score += 20
            ai_settings.menu = "score"
    elif ai_settings.menu == "score":
        if play_again_clicked:
            sb.reset_score()
            ai_settings.menu = "topics"

def update_screen(ai_settings, screen, button, sb):
    screen.fill(ai_settings.bg_color)
    pygame.font.init()
    # Draw the score information.
    if ai_settings.menu == "main":
        button.start()
        sb.title()
    elif ai_settings.menu == "tutorial":
        button.tutorial()
    elif ai_settings.menu == "topics":
        button.topics()
    elif ai_settings.menu == "array_no1":
        button.no1()
    elif ai_settings.menu == "array_no2":
        button.no2()
    elif ai_settings.menu == "array_no3":
        button.no3()
    elif ai_settings.menu == "array_no4":
        button.no4()
    elif ai_settings.menu == "array_no5":
        button.no5()
    elif ai_settings.menu == "operators_no1":
        button.no6()
    elif ai_settings.menu == "operators_no2":
        button.no7()
    elif ai_settings.menu == "operators_no3":
        button.no8()
    elif ai_settings.menu == "operators_no4":
        button.no9()
    elif ai_settings.menu == "operators_no5":
        button.no10()
    elif ai_settings.menu == "loops_no1":
        button.no11()
    elif ai_settings.menu == "loops_no2":
        button.no12()
    elif ai_settings.menu == "loops_no3":
        button.no13()
    elif ai_settings.menu == "loops_no4":
        button.no14()
    elif ai_settings.menu == "loops_no5":
        button.no15()
    elif ai_settings.menu == "score":
        sb.show_score()
        button.retry()

    # Make the most recently drawn screen visible.
    pygame.display.flip()