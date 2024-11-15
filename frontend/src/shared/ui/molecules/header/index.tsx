import Text from '../../atoms/text/index'
import * as S from './styles'

interface Props {
  icon: JSX.Element
  title: string
}

const Header = ({ icon, title }: Props) => {
  return (
    <S.Container>
      <S.WrapperTitleAndIcon>
        <S.Icon>
          {icon}
        </S.Icon>
        <Text
          as='h1'
          size={1.8}
          fontFamily='Public Sans'
          weight={700}
        >
          {title}
        </Text>
      </S.WrapperTitleAndIcon>
    </S.Container>
  )
}

export default Header