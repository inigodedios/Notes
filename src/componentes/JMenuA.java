package componentes;

import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.JMenuBar;
import javax.swing.*;

import java.awt.*;
import java.awt.event.KeyEvent;

public class JMenuA extends JFrame {
    //Para crear menús --> 1º JMenuBar, 2º Jmenu, 3º JMenuItem

    private JPanel p;
    private JMenuBar menuBar;
    private JMenu menu1, menu2, menu3, menu4;
    private JMenuItem menuItem11, menuItem21, menuItem31, menuItem32;

    public JMenuA (){
        p = new JPanel(new BorderLayout());
        this.setSize(310, 210);
        this.setLocationRelativeTo(null);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        menuBar = new JMenuBar();

        menu1 = new JMenu("Menú1");
        menu2 = new JMenu("Menú2");
        menu3 = new JMenu("Menú3");
        menu4 = new JMenu("Menú4");
        menu2.setMnemonic( KeyEvent.VK_V );

        menuItem11 = new JMenuItem("Item11");
        menuItem21 = new JMenuItem("Item21");
        menuItem31 = new JMenuItem("Item31");
        menuItem32 = new JMenuItem("Item32");

        menuBar.add(menu1);
        menuBar.add(menu2);
        menuBar.add(menu3);

        menu1.add(menuItem11);
        menu2.add(menuItem21);
        menu3.add(menuItem31);
        menu3.add(menuItem32);

        setJMenuBar(menuBar);

        menuItem11.addActionListener(
                (e) -> metodoLambda());

    }

    private void metodoLambda() {}

    public static void main(String[] args) {
        JMenuA v = new JMenuA();
        v.setVisible(true);
    }

}
