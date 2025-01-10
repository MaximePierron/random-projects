<?php
/**
 * ParallaxMenu class.
 *
 * @category   Class
 * @package    ElementorCustom
 * @subpackage WordPress
 * @author     Maxime Pierron <maxime@pierron.com>
 * @copyright  2023 Maxime Pierron
 * @license    https://opensource.org/licenses/GPL-3.0 GPL-3.0-only
 * @link       link(https://example.com/,
 *             Build Custom Elementor Widgets)
 * @since      1.0.0
 * php version 8.2.3
 */
namespace ElementorCustom\Widgets;

use ElementorPro\Base\Base_Widget;
use Elementor\Controls_Manager;
// Security Note: Blocks direct access to the plugin PHP files.
defined( 'ABSPATH' ) || die();
/**
 * ParallaxMenu widget class.
 *
 * @since 1.0.0
 */
class ParallaxMenu extends Base_Widget {
	/**
	 * Class constructor.
	 *
	 * @param array $data Widget data.
	 * @param array $args Widget arguments.
	 */
	public function __construct( $data = array(), $args = null ) {
		parent::__construct( $data, $args );
		wp_register_style( 'parallaxmenu', plugins_url( '/assets/css/parallaxmenu.css', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
		wp_register_script( 'parallaxmenu', plugins_url( '/assets/js/parallaxmenu.js', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
	}
	/**
	 * Retrieve the widget name.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget name.
	 */
	public function get_name() {
		return 'parallax-menu';
	}
	/**
	 * Retrieve the widget title.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget title.
	 */
	public function get_title() {
		return __( 'Parallax Menu', 'elementor-custom' );
	}
	/**
	 * Retrieve the widget icon.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget icon.
	 */
	public function get_icon() {
		return 'eicon-parallax';
	}
	/**
	 * Retrieve the list of categories the widget belongs to.
	 *
	 * Used to determine where to display the widget in the editor.
	 *
	 * Note that currently Elementor supports only one category.
	 * When multiple categories passed, Elementor uses the first one.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return array Widget categories.
	 */
	public function get_categories() {
		return array( 'elementor-custom-widgets' );
	}
	
	/**
	 * Enqueue styles.
	 */
	public function get_style_depends() {
		return array( 'parallaxmenu' );
	}
	/**
	 * Enqueue scripts.
	 */
	public function get_script_depends() {
		if (\Elementor\Plugin::$instance->editor->is_edit_mode() || \Elementor\Plugin::$instance->preview->is_preview_mode()) {
			return [];
		} else {
			return array( 'parallaxmenu' );
		}
		
	}

	/**
	 * Register the widget controls.
	 *
	 * Adds different input fields to allow the user to change and customize the widget settings.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function _register_controls() {

		$this->start_controls_section(
			'content_section',
			[
				'label' => __( 'Content', 'elementor-custom' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);

        $this->add_control(
			'background_color',
			[
				'label' => esc_html__( 'Background Color', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} .parallax-menu' => 'background-color: {{VALUE}}',
				],
                'default' => 'rgb(20, 20, 20)'
			]
		);

        $this->add_control(
			'background_image',
			[
				'label' => esc_html__( 'Choose Background Image', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'default' => [
					'url' => \Elementor\Utils::get_placeholder_image_src(),
				],
			]
		);

        $this->add_control(
			'background_image_opacity',
			[
				'label' => esc_html__( 'Background Image Opacity', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 0,
				'max' => 1,
				'step' => 0.05,
				'default' => 0.15,
			]
		);

        $this->add_control(
			'pattern_size',
			[
				'label' => esc_html__( 'Pattern size', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 1,
				'max' => 70,
				'step' => 1,
				'default' => 9,
			]
		);

        $this->add_control(
			'pattern_diffusion',
			[
				'label' => esc_html__( 'Pattern Diffusion', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 1,
				'max' => 100,
				'step' => 1,
				'default' => 9,
			]
		);

        $this->add_control(
			'pattern_r',
			[
				'label' => esc_html__( 'R', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 0,
				'max' => 255,
				'step' => 1,
				'default' => 255,
			]
		);

        $this->add_control(
			'pattern_g',
			[
				'label' => esc_html__( 'G', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 0,
				'max' => 255,
				'step' => 1,
				'default' => 255,
			]
		);

        $this->add_control(
			'pattern_b',
			[
				'label' => esc_html__( 'B', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 0,
				'max' => 255,
				'step' => 1,
				'default' => 255,
			]
		);

        $this->add_control(
			'pattern_a',
			[
				'label' => esc_html__( 'Alpha', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 0,
				'max' => 1,
				'step' => 0.05,
				'default' => 0.1,
			]
		);

		// $this->add_control(
		// 	'pattern_color',
		// 	[
		// 		'label' => esc_html__( 'Pattern Color', 'elementor-custom' ),
		// 		'type' => \Elementor\Controls_Manager::COLOR,
        //         'default' => 'rgba(255, 255, 255, 0.1)'
		// 	]
		// );

		$this->add_control(
			'font_family',
			[
				'label' => esc_html__( 'Font Family', 'textdomain' ),
				'type' => \Elementor\Controls_Manager::FONT,
				'default' => "'Open Sans', sans-serif",
				'selectors' => [
					'{{WRAPPER}} .parallax-menu-item' => 'font-family: {{VALUE}}',
				],
			]
		);

		$this->add_control(
			'font_min',
			[
				'label' => esc_html__( 'Font min size in rem', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 0,
				'max' => 50,
				'step' => 0.1,
				'default' => 3,
			]
		);

		$this->add_control(
			'font_max',
			[
				'label' => esc_html__( 'Font max size in rem', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 1,
				'max' => 50,
				'step' => 0.1,
				'default' => 8,
			]
		);

		$this->add_control(
			'font_value',
			[
				'label' => esc_html__( 'Font desired size in viewportwidth percentage', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 1,
				'max' => 50,
				'step' => 0.5,
				'default' => 8,
			]
		);

        $repeater = new \Elementor\Repeater();

		$repeater->add_control(
			'menu_item_title',
			[
				'label' => esc_html__( 'Add a menu item title', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => esc_html__( 'Menu Item Title' , 'elementor-custom' ),
				'label_block' => true,
			]
		);

        $repeater->add_control(
			'menu_item_url',
			[
				'label' => esc_html__( 'Add a menu item url', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::URL,
                'placeholder' => esc_html__( 'https://your-link.com', 'elementor-custom' ),
				'options' => [ 'url', 'is_external', 'nofollow' ],
				'default' => [
					'url' => '',
					'is_external' => true,
					'nofollow' => true,
				],
				'label_block' => true,
			]
		);

        $this->add_control(
			'list',
			[
				'label' => esc_html__( 'Add your menu items', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::REPEATER,
				'fields' => $repeater->get_controls(),
				'default' => [
					[
						'menu-item-title' => esc_html__( 'Menu Item #1', 'elementor-custom' ),
						'menu-item-url' => esc_html__( 'https://your-link.com', 'elementor-custom' ),
					]
				],
			]
		);

		$this->end_controls_section();
	}
	/**
	 * Render the widget output on the frontend.
	 *
	 * Written in PHP and used to generate the final HTML.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function render() {
		$settings = $this->get_settings_for_display();
        ?>
        <div id="parallax-menu" class="parallax-menu">
            <div id="parallax-menu-items">
        <?php
                if ( $settings['list'] ) {
                    foreach (  $settings['list'] as $item ) {
                        echo '<a href="' . $item['menu_item_url']['url'] .'" class="parallax-menu-item parallax-menu-item-' . esc_attr( $item['_id'] ) . '" style="font-size: clamp(' . $settings['font_min'] . 'rem, ' . $settings['font_value'] . 'vw, ' . $settings['font_max'] . 'rem)">' . $item['menu_item_title'] . '</a>';
                    }
                }
        ?>
            </div>
            <?php
            echo '<div id="parallax-menu-background-pattern" style="background-image: radial-gradient(rgba(' . $settings[pattern_r] . ',' . $settings[pattern_g] . ',' . $settings[pattern_b] . ',' . $settings[pattern_a] . ') ' . $settings[pattern_size] . '%,transparent ' . $settings[pattern_diffusion] . '%);"></div>';
            // echo '<div id="parallax-menu-background-pattern" style="background-image: radial-gradient(' . $settings[pattern_color] . ') ' . $settings[pattern_size] . '%,transparent ' . $settings[pattern_diffusion] . '%);"></div>';
            echo '<div id="parallax-menu-background-image" style="opacity:' . $settings['background_image_opacity'] . ';background-image: url(' . $settings['background_image']['url'] . ')"></div>';
            echo '</div>';
	}

	protected function content_template() {
		?>
        <div id="parallax-menu">
            <div id="parallax-menu-items">
                <# if ( settings.list.length ) { #>
                    <# _.each( settings.list, function( item ) { #>
                        <a src="{{ item.menu_item_url }}" class="parallax-menu-item parallax-menu-item-{{ item._id }}"> {{{ item.menu_item_title }}} </a>
                    <# }); #>
                <# } #>
            </div>
            <div id="parallax-menu-background-pattern"></div>
            <div id="parallax-menu-background-image" style="background-image: url('{{ settings.background_image.url }}')"></div>
        </div>
		<?php
	}
}