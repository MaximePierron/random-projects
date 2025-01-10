<?php
/**
 * FuturisticCard class.
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
 * FuturisticCard widget class.
 *
 * @since 1.0.0
 */
class FuturisticCard extends Base_Widget {
	/**
	 * Class constructor.
	 *
	 * @param array $data Widget data.
	 * @param array $args Widget arguments.
	 */
	public function __construct( $data = array(), $args = null ) {
		parent::__construct( $data, $args );
		wp_register_style( 'futuristiccard', plugins_url( '/assets/css/futuristiccard.css', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
		wp_register_script( 'futuristiccard', plugins_url( '/assets/js/texteffect.js', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
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
		return 'futuristic-card';
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
		return __( 'Futuristic Card', 'elementor-custom' );
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
		return 'eicon-blockquote';
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
		return array( 'futuristiccard' );
	}
	/**
	 * Enqueue scripts.
	 */
	public function get_script_depends() {
		if (\Elementor\Plugin::$instance->editor->is_edit_mode() || \Elementor\Plugin::$instance->preview->is_preview_mode()) {
			return [];
		} else {
			return array( 'futuristiccard' );
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
			'primary_r',
			[
				'label' => esc_html__( 'R', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 0,
				'max' => 255,
				'step' => 1,
				'default' => 33,
			]
		);

        $this->add_control(
			'primary_g',
			[
				'label' => esc_html__( 'G', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 0,
				'max' => 255,
				'step' => 1,
				'default' => 150,
			]
		);

        $this->add_control(
			'primary_b',
			[
				'label' => esc_html__( 'B', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::NUMBER,
				'min' => 0,
				'max' => 255,
				'step' => 1,
				'default' => 243,
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
			'icon',
			[
				'label' => esc_html__( 'Icon', 'textdomain' ),
				'type' => \Elementor\Controls_Manager::ICONS,
			]
		);

		$this->add_control(
			'card_title',
			[
				'label' => esc_html__( 'Add a title', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => esc_html__( 'Title' , 'elementor-custom' ),
				'label_block' => true,
			]
		);

        $this->add_control(
			'card_sub_title',
			[
				'label' => esc_html__( 'Add a sub title', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => esc_html__( 'Subtitle' , 'elementor-custom' ),
				'label_block' => true,
			]
		);

        $this->add_control(
			'card_sub_title_url',
			[
				'label' => esc_html__( 'Add a url to the subtitle', 'elementor-custom' ),
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
        echo '<style> :root{--primary-rgb:' . $settings[primary_r] . ' ' . $settings[primary_g] . ' ' . $settings[primary_b] . '}</style>';
        echo '<div class="screen">';
        echo '<div class="screen-image" style="background-image: url(' . $settings['background_image']['url'] . ')"></div>';
        ?>
            <div class="screen-overlay"></div>  
            <div class="screen-content">
                <div class="screen-icon">
                    <?php \Elementor\Icons_Manager::render_icon( $settings['icon'], [ 'aria-hidden' => 'true' ] ); ?>
                </div>
                <div class="screen-user">
        <?php
                echo '<span class="name" data-value="' . $settings['card_title'] . '">' . $settings['card_title'] . '</span>';
                echo '<a class="link" href="' . $settings['card_sub_title_url'] . '" target="_blank">' . $settings['card_sub_title'] . '</a>'
        ?>
                </div>
            </div>
        </div>
        <?php
	}

	protected function content_template() {
		?>
        <#
		    var iconHTML = elementor.helpers.renderIcon( view, settings.selected_icon, { 'aria-hidden': true }, 'i' , 'object' );
		#>
        <style> :root{--primary-rgb:"{{ settings.primary_color }}" }</style>
        <div class="screen">
            <div class="screen-image" style="background-image: url({{settings.background_image.url}})"></div>
            <div class="screen-overlay"></div>  
            <div class="screen-content">
                <div class="screen-icon">
                    {{{ iconHTML.value }}}
                </div>
                <div class="screen-user">
                <span class="name" data-value="{{settings.card_title}}">{{{ settings.card_title }}}</span>
                <a class="link" href="{{settings.card_sub_title_url}}" target="_blank">{{{ settings.card_sub_title }}}</a>
                </div>
            </div>
        </div>
		<?php
	}
}